from django.db import models

class TouristSite(models.Model):
    SITE_TYPE_CHOICES = [
        ('natural', 'Natural'),
        ('cultural', 'Cultural'),
        ('other', 'Other'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150, blank=True, null=True)
    site_type = models.CharField(max_length=20, choices=SITE_TYPE_CHOICES, default='other')
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'tourist_sites'
        managed = True
        
    def __str__(self):
        return self.name
