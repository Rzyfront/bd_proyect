from django.db import models
from MyApps.tourist_sites.models import TouristSite

class TourPlan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    total_duration = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tourist_sites = models.ManyToManyField(TouristSite, through='TourPlanTouristSite')
    
    class Meta:
        db_table = 'tour_plans'
        managed = True
        
    def __str__(self):
        return self.name

class TourPlanTouristSite(models.Model):
    tour_plan = models.ForeignKey(TourPlan, on_delete=models.CASCADE, db_column='tour_plan_id')
    tourist_site = models.ForeignKey(TouristSite, on_delete=models.CASCADE, db_column='tourist_site_id')
    visit_order = models.IntegerField()
    stay_time = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'tour_plan_tourist_site'
        managed = True
        unique_together = ('tour_plan', 'tourist_site')
        
    def __str__(self):
        return f"{self.tour_plan.name} - {self.tourist_site.name}"
