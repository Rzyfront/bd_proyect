from django.contrib import admin
from .models import TouristSite

@admin.register(TouristSite)
class TouristSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'site_type')
    list_filter = ('site_type',)
    search_fields = ('name', 'location')
    ordering = ('name',)
    list_per_page = 25
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'location', 'site_type')
        }),
        ('Descripción', {
            'fields': ('description',)
        }),
    )
