from django.shortcuts import render
from rest_framework import viewsets
from .models import TourRequest
from .serializers import TourRequestSerializer

# Create your views here.

class TourRequestViewSet(viewsets.ModelViewSet):
    """CRUD API for Tour Requests"""
    queryset = TourRequest.objects.all()
    serializer_class = TourRequestSerializer
