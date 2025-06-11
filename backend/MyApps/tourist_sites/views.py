from django.shortcuts import render
from rest_framework import viewsets
from .models import TouristSite
from .serializers import TouristSiteSerializer

# Create your views here.

class TouristSiteViewSet(viewsets.ModelViewSet):
    """CRUD API for Tourist Sites"""
    queryset = TouristSite.objects.all()
    serializer_class = TouristSiteSerializer
