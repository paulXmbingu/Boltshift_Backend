from rest_framework import serializers
from .models import (
    DetailModel, SummaryDescriptionModel, BrandModel,
    CategoryModel, SubCategoryModel, PhotosModel,
    VideosModel, ShowRatingModel, ReviewModel, 
    InventoryMeterModel, Option1Model, Option2Model, 
    TagsModel, DescriptionModel, SpecificationModel, 
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





class VideosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideosModel
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





class Option1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option1Model
        fields = '__all__'





class Option2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option2Model
        fields = '__all__'





class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        fields = '__all__'





class DescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = '__all__'





class SpecificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationModel
        fields = '__all__'