from django.contrib import admin
from .models import (
    DetailModel,CategoryModel, SubCategoryModel,
    PhotosModel, VideosModel, BrandModel,
    ShowRatingModel,ReviewModel, InventoryMeterModel,
    Option1Model, Option2Model, TagsModel,
    DescriptionModel, SpecificationModel, SummaryDescriptionModel
)





@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku_code'] 
    search_fields = ['name', 'sku_code']





@admin.register(SummaryDescriptionModel)
class SummaryDescriptionModelAdmin(admin.ModelAdmin):
    list_display = ['summary_description'] 
    search_fields = ['summary_description'] 





@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['brand']
    search_fields = ['brand']
 




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





@admin.register(ShowRatingModel)
class ShowRatingModelAdmin(admin.ModelAdmin):
    list_display = ['average_star_ratings', 'five_star_rating', 'four_star_rating', 'three_star_rating', 'two_star_rating', 'one_star_rating', ]
    search_fields = ['average_star_ratings', 'five_star_rating', 'four_star_rating', 'three_star_rating', 'two_star_rating', 'one_star_rating', ]





@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['reviews_count']
    search_fields = ['reviews_count']





@admin.register(InventoryMeterModel)
class InventoryMeterModelAdmin(admin.ModelAdmin):
    list_display = ['remaining_items', 'total_items']
    search_fields = ['remaining_items', 'total_items']





@admin.register(Option1Model)
class Option1ModelAdmin(admin.ModelAdmin):
    list_display = ['option_1_selector']
    search_fields = ['option_1_selector']





@admin.register(Option2Model)
class Option2ModelAdmin(admin.ModelAdmin):
    list_display = ['option_2_selector']
    search_fields = ['option_2_selector']





@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']
    search_fields = ['tag_list']





@admin.register(DescriptionModel)
class DescriptionModelAdmin(admin.ModelAdmin):
    list_display = ['long_description']
    search_fields = ['long_description']





@admin.register(SpecificationModel)
class SpecificationModelAdmin(admin.ModelAdmin):
    list_display = ['specification']
    search_fields = ['specification']