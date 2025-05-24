from django.db import models
from MyApps.customers.models import Customer
from MyApps.tour_plans.models import TourPlan

class TourRequest(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    tour_plan = models.ForeignKey(TourPlan, on_delete=models.CASCADE, db_column='tour_plan_id')
    request_date = models.DateField()
    tour_date = models.DateField()
    people_count = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'tour_requests'
        managed = True
        
    def __str__(self):
        return f"{self.customer.name} - {self.tour_plan.name}"
