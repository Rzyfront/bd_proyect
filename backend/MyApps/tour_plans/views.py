from django.shortcuts import render
from rest_framework import viewsets
from .models import TourPlan, TourPlanTouristSite
from .serializers import TourPlanSerializer, TourPlanTouristSiteSerializer

# Create your views here.

class TourPlanViewSet(viewsets.ModelViewSet):
    """CRUD API for Tour Plans"""
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer

class TourPlanTouristSiteViewSet(viewsets.ModelViewSet):
    """CRUD API for TourPlanTouristSite relations"""
    queryset = TourPlanTouristSite.objects.all()
    serializer_class = TourPlanTouristSiteSerializer
