from django.contrib import admin
from .models import DetailModel,CategoryModel, SubCategoryModel, PhotosModel, VideosModel, BrandModel, ShowRatingModel,ReviewModel



@admin.register(DetailModel)
class DetailModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku_code'] 
    search_fields = ['name', 'sku_code'] 



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