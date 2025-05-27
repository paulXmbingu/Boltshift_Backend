from django.contrib import admin
from .models import DetailModel, CategoryModel, SubCategoryModel



''' DETAIL MODEL ADMIN CLASS'''
@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku_code', 'category', 'sub_category'] 
    search_fields = ['name', 'sku_code', 'category__category', 'sub_category__sub_category'] 
    
    

''' CATEGORY MODEL ADMIN CLASS'''
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category']
    search_fields = ['category']



''' SUBCATEGORY MODEL ADMIN CLASS'''
@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['sub_category']
    search_fields = ['sub_category']