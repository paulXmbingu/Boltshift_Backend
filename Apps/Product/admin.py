from django.contrib import admin
from .models import DetailModel

@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku_code', 'price', 'currency')
    search_fields = ('name', 'sku_code')
    list_filter = ('currency',)
    ordering = ('name',)
    readonly_fields = ()
    
