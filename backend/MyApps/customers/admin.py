from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'nationality')
    list_filter = ('nationality',)
    search_fields = ('name', 'email', 'identity_document')
    ordering = ('name',)
    list_per_page = 25
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Documentación', {
            'fields': ('identity_document', 'nationality')
        }),
    )
