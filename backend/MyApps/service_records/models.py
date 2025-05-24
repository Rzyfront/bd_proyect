from django.db import models
from MyApps.tour_requests.models import TourRequest

class ServiceRecord(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    id = models.AutoField(primary_key=True)
    tour_request = models.ForeignKey(TourRequest, on_delete=models.CASCADE, db_column='tour_request_id')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    record_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'service_records'
        managed = True
        
    def __str__(self):
        return f"{self.tour_request} - {self.status}"
