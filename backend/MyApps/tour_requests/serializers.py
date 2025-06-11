from rest_framework import serializers
from .models import TourRequest

class TourRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourRequest
        fields = '__all__'
