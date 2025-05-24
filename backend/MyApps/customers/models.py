from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    identity_document = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        db_table = 'customers'
        managed = True
        
    def __str__(self):
        return self.name
