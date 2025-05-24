from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
import random
from datetime import date, timedelta

from MyApps.customers.models import Customer
from MyApps.tourist_sites.models import TouristSite
from MyApps.tour_plans.models import TourPlan, TourPlanTouristSite
from MyApps.tour_requests.models import TourRequest
from MyApps.service_records.models import ServiceRecord

class Command(BaseCommand):
    help = 'Poblar la base de datos con datos de prueba usando Faker'

    def handle(self, *args, **options):
        fake = Faker(['es_ES', 'es_CO', 'es_MX'])  # Español de España, Colombia y México
        
        self.stdout.write(self.style.SUCCESS('🚀 Iniciando población de la base de datos...'))
        
        with transaction.atomic():
            # Limpiar datos existentes
            self.stdout.write('🧹 Limpiando datos existentes...')
            ServiceRecord.objects.all().delete()
            TourRequest.objects.all().delete()
            TourPlanTouristSite.objects.all().delete()
            TourPlan.objects.all().delete()
            TouristSite.objects.all().delete()
            Customer.objects.all().delete()
            
            # Crear clientes
            self.stdout.write('👥 Creando 30 clientes...')
            customers = []
            for _ in range(30):
                customer = Customer(
                    name=fake.name(),
                    email=fake.unique.email(),
                    phone=fake.phone_number()[:20],
                    identity_document=fake.unique.random_number(digits=10, fix_len=True),
                    nationality=fake.country()[:50]
                )
                customers.append(customer)
            Customer.objects.bulk_create(customers)
            
            # Crear sitios turísticos
            self.stdout.write('🏛️ Creando 15 sitios turísticos...')
            site_types = ['natural', 'cultural', 'other']
            tourist_sites = []
            
            # Sitios predefinidos más realistas
            predefined_sites = [
                ('Cartagena Histórica', 'Cartagena, Colombia', 'cultural', 'Centro histórico amurallado'),
                ('Parque Tayrona', 'Santa Marta, Colombia', 'natural', 'Parque nacional con playas vírgenes'),
                ('Machu Picchu', 'Cusco, Perú', 'cultural', 'Ciudadela inca en los Andes'),
                ('Salar de Uyuni', 'Potosí, Bolivia', 'natural', 'El mayor desierto de sal del mundo'),
                ('Chichen Itzá', 'Yucatán, México', 'cultural', 'Antigua ciudad maya'),
                ('Cataratas del Iguazú', 'Argentina/Brasil', 'natural', 'Sistema de cascadas espectacular'),
                ('Plaza de Armas', 'Lima, Perú', 'cultural', 'Centro histórico de Lima'),
                ('Laguna Colorada', 'Potosí, Bolivia', 'natural', 'Laguna de color rojizo por microorganismos'),
            ]
            
            for name, location, site_type, description in predefined_sites:
                tourist_site = TouristSite(
                    name=name,
                    location=location,
                    site_type=site_type,
                    description=description
                )
                tourist_sites.append(tourist_site)
            
            # Completar con sitios generados aleatoriamente
            remaining_sites = 15 - len(predefined_sites)
            for _ in range(max(0, remaining_sites)):
                tourist_site = TouristSite(
                    name=f"{fake.word().title()} {random.choice(['Nacional', 'Colonial', 'Histórico', 'Natural'])}",
                    location=f"{fake.city()}, {fake.country()}",
                    site_type=random.choice(site_types),
                    description=fake.text(max_nb_chars=200)
                )
                tourist_sites.append(tourist_site)
            
            TouristSite.objects.bulk_create(tourist_sites)
            
            # Crear planes turísticos
            self.stdout.write('🗺️ Creando 10 planes turísticos...')
            tour_plans = []
            plan_names = [
                'Tour Histórico Colonial', 'Aventura en la Naturaleza', 'Ruta Cultural',
                'Expedición Fotográfica', 'Tour Gastronómico', 'Caminata Ecológica',
                'Experiencia Arqueológica', 'Tour Nocturno', 'Aventura Extrema',
                'Turismo Rural', 'Tour Familiar', 'Escapada Romántica'
            ]
            
            for i in range(10):
                tour_plan = TourPlan(
                    name=f"{random.choice(plan_names)} {i+1}",
                    description=fake.text(max_nb_chars=300),
                    total_duration=random.randint(120, 720),  # 2 a 12 horas
                    price=round(random.uniform(50.0, 500.0), 2)
                )
                tour_plans.append(tour_plan)
            TourPlan.objects.bulk_create(tour_plans)
            
            # Crear relaciones many-to-many entre planes y sitios
            self.stdout.write('🔗 Creando relaciones entre planes y sitios...')
            all_plans = list(TourPlan.objects.all())
            all_sites = list(TouristSite.objects.all())
            
            plan_site_relations = []
            for plan in all_plans:
                # Cada plan tendrá entre 2 y 5 sitios
                sites_for_plan = random.sample(all_sites, random.randint(2, min(5, len(all_sites))))
                for i, site in enumerate(sites_for_plan, 1):
                    relation = TourPlanTouristSite(
                        tour_plan=plan,
                        tourist_site=site,
                        visit_order=i,
                        stay_time=random.randint(30, 180)  # 30 minutos a 3 horas
                    )
                    plan_site_relations.append(relation)
            TourPlanTouristSite.objects.bulk_create(plan_site_relations)
            
            # Crear solicitudes de tour
            self.stdout.write('📋 Creando 50 solicitudes de tour...')
            all_customers = list(Customer.objects.all())
            tour_requests = []
            
            for _ in range(50):
                request_date = fake.date_between(start_date='-3m', end_date='today')
                tour_date = fake.date_between(start_date=request_date, end_date='+6m')
                
                tour_request = TourRequest(
                    customer=random.choice(all_customers),
                    tour_plan=random.choice(all_plans),
                    request_date=request_date,
                    tour_date=tour_date,
                    people_count=random.randint(1, 8),
                    notes=fake.text(max_nb_chars=200) if random.choice([True, False]) else None
                )
                tour_requests.append(tour_request)
            TourRequest.objects.bulk_create(tour_requests)
            
            # Crear registros de servicio
            self.stdout.write('📊 Creando registros de servicio...')
            all_requests = list(TourRequest.objects.all())
            service_records = []
            statuses = ['confirmed', 'cancelled', 'completed']
            
            for request in all_requests:
                # 80% de probabilidad de tener registro de servicio
                if random.random() < 0.8:
                    # El estado depende de la fecha del tour
                    if request.tour_date < date.today():
                        status = random.choices(
                            ['completed', 'cancelled'], 
                            weights=[85, 15]  # 85% completado, 15% cancelado
                        )[0]
                    elif request.tour_date == date.today():
                        status = 'confirmed'
                    else:
                        status = random.choices(
                            ['confirmed', 'cancelled'], 
                            weights=[90, 10]  # 90% confirmado, 10% cancelado
                        )[0]
                    
                    record_date = fake.date_between(
                        start_date=request.request_date,
                        end_date=min(request.tour_date, date.today())
                    )
                    
                    service_record = ServiceRecord(
                        tour_request=request,
                        status=status,
                        record_date=record_date,
                        comments=fake.text(max_nb_chars=150) if random.choice([True, False]) else None
                    )
                    service_records.append(service_record)
            
            ServiceRecord.objects.bulk_create(service_records)
            
            # Mostrar estadísticas finales
            self.stdout.write(self.style.SUCCESS('\n✅ ¡Base de datos poblada exitosamente!'))
            self.stdout.write(f'📊 Estadísticas finales:')
            self.stdout.write(f'   • Clientes: {Customer.objects.count()}')
            self.stdout.write(f'   • Sitios turísticos: {TouristSite.objects.count()}')
            self.stdout.write(f'   • Planes turísticos: {TourPlan.objects.count()}')
            self.stdout.write(f'   • Relaciones plan-sitio: {TourPlanTouristSite.objects.count()}')
            self.stdout.write(f'   • Solicitudes de tour: {TourRequest.objects.count()}')
            self.stdout.write(f'   • Registros de servicio: {ServiceRecord.objects.count()}')
