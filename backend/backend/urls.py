"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from MyApps.customers.views import CustomerViewSet
from MyApps.tourist_sites.views import TouristSiteViewSet
from MyApps.tour_plans.views import TourPlanViewSet, TourPlanTouristSiteViewSet
from MyApps.tour_requests.views import TourRequestViewSet
from MyApps.service_records.views import ServiceRecordViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'tourist-sites', TouristSiteViewSet)
router.register(r'tour-plans', TourPlanViewSet)
router.register(r'tour-plan-sites', TourPlanTouristSiteViewSet)
router.register(r'tour-requests', TourRequestViewSet)
router.register(r'service-records', ServiceRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
