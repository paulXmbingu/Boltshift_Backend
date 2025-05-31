from rest_framework import serializers
from .models import (
    DetailModel, SummaryDescriptionModel, BrandModel,
    CategoryModel, SubCategoryModel, PhotosModel, 
    ShowRatingModel, ReviewModel, InventoryMeterModel
)





class DetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailModel
        fields = '__all__'





class SummaryDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryDescriptionModel
        fields = '__all__'





class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'





class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'





class SubCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = '__all__'





class PhotosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotosModel
        fields = '__all__'





class ShowRatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowRatingModel
        fields = '__all__'





class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'





class InventoryMeterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMeterModel
        fields = '__all__'