from django.contrib import admin
from .models import DetailModel, CategoryModel, SubCategoryModel, PhotosModel, VideosModel



@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku_code'] 
    search_fields = ['name', 'sku_code'] 
    
    

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category']
    search_fields = ['category']



@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['sub_category']
    search_fields = ['sub_category']



@admin.register(PhotosModel)
class PhotosModelAdmin(admin.ModelAdmin):
    list_display = ['product_photos']
    search_fields = ['product_photos']



@admin.register(VideosModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['product_videos']
    search_fields = ['product_videos']



