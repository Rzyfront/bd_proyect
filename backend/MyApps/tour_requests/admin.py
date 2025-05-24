from django.contrib import admin
from .models import TourRequest

@admin.register(TourRequest)
class TourRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'tour_plan', 'request_date', 'tour_date', 'people_count', 'get_status')
    list_filter = ('request_date', 'tour_date', 'people_count')
    search_fields = ('customer__name', 'tour_plan__name', 'notes')
    ordering = ('-request_date',)
    list_per_page = 25
    date_hierarchy = 'tour_date'
    
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('customer',)
        }),
        ('Detalles del Tour', {
            'fields': ('tour_plan', 'people_count')
        }),
        ('Fechas', {
            'fields': ('request_date', 'tour_date')
        }),
        ('Observaciones', {
            'fields': ('notes',)
        }),
    )
    
    def get_status(self, obj):
        # Obtener el estado desde ServiceRecord si existe
        service_record = obj.servicerecord_set.first()
        if service_record:
            return service_record.status
        return 'Sin registro'
    get_status.short_description = 'Estado'
