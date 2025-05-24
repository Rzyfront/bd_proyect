from django.contrib import admin
from .models import TourPlan, TourPlanTouristSite

class TourPlanTouristSiteInline(admin.TabularInline):
    model = TourPlanTouristSite
    extra = 1
    ordering = ('visit_order',)
    fields = ('tourist_site', 'visit_order', 'stay_time')

@admin.register(TourPlan)
class TourPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'total_duration', 'get_sites_count')
    list_filter = ('price',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 25
    inlines = [TourPlanTouristSiteInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description')
        }),
        ('Detalles del Tour', {
            'fields': ('total_duration', 'price')
        }),
    )
    
    def get_sites_count(self, obj):
        return obj.tourist_sites.count()
    get_sites_count.short_description = 'Sitios'

@admin.register(TourPlanTouristSite)
class TourPlanTouristSiteAdmin(admin.ModelAdmin):
    list_display = ('tour_plan', 'tourist_site', 'visit_order', 'stay_time')
    list_filter = ('tour_plan', 'tourist_site')
    ordering = ('tour_plan', 'visit_order')
