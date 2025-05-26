from django.contrib import admin
from .models import DetailModel, CategoryModel


@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ('name','sku_code', 'currency', 'price')
    search_fields = ('name', 'brand', 'sku_code',)
    
    
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'sub_category')
    search_fields = ('category', 'sub_category')
