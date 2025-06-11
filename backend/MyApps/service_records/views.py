from django.shortcuts import render
from rest_framework import viewsets
from .models import ServiceRecord
from .serializers import ServiceRecordSerializer

# Create your views here.

class ServiceRecordViewSet(viewsets.ModelViewSet):
    """CRUD API for Service Records"""
    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordSerializer
