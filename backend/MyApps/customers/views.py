from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    """CRUD API for Customers"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
