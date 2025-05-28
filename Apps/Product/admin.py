from django.contrib import admin
from .models import DetailModel, CategoryModel, SubCategoryModel



@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku_code', 'category', 'sub_category'] 
    search_fields = ['name', 'sku_code', 'category__category', 'sub_category__sub_category'] 
    
    

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category']
    search_fields = ['category']



@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['sub_category']
    search_fields = ['sub_category']