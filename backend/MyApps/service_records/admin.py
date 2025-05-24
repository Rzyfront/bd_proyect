from django.contrib import admin
from .models import ServiceRecord

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour_request', 'status', 'record_date', 'get_customer', 'get_tour_plan')
    list_filter = ('status', 'record_date')
    search_fields = ('tour_request__customer__name', 'tour_request__tour_plan__name', 'comments')
    ordering = ('-record_date',)
    list_per_page = 25
    date_hierarchy = 'record_date'
    
    fieldsets = (
        ('Información del Registro', {
            'fields': ('tour_request', 'status', 'record_date')
        }),
        ('Comentarios', {
            'fields': ('comments',)
        }),
    )
    
    def get_customer(self, obj):
        return obj.tour_request.customer.name
    get_customer.short_description = 'Cliente'
    
    def get_tour_plan(self, obj):
        return obj.tour_request.tour_plan.name
    get_tour_plan.short_description = 'Plan de Tour'
