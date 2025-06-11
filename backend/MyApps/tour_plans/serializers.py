from rest_framework import serializers
from .models import TourPlan, TourPlanTouristSite

class TourPlanTouristSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPlanTouristSite
        fields = '__all__'

class TourPlanSerializer(serializers.ModelSerializer):
    tourist_sites = TourPlanTouristSiteSerializer(many=True, read_only=True)
    class Meta:
        model = TourPlan
        fields = '__all__'
