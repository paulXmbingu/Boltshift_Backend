from rest_framework import generics
from .models import (
    DetailModel, SummaryDescriptionModel, BrandModel,
    CategoryModel, SubCategoryModel, PhotosModel, 
    VideosModel, ShowRatingModel, ReviewModel,
    InventoryMeterModel, Option1Model, Option2Model,
    TagsModel, DescriptionModel, 
)
from .serializers import (
    DetailModelSerializer, SummaryDescriptionSerializer, BrandModelSerializer,
    CategoryModelSerializer, SubCategoryModelSerializer, PhotosModelSerializer,
    VideosModelSerializer, ShowRatingModelSerializer, ReviewModelSerializer,
    InventoryMeterModelSerializer, Option1ModelSerializer, Option2ModelSerializer,
    TagsModelSerializer, DescriptionModelSerializer, 
)





class DetailListView(generics.ListAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailCreateView(generics.CreateAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailRetrieveView(generics.RetrieveAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailUpdateView(generics.UpdateAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailDestroyView(generics.DestroyAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer





class SummaryDescriptionListView(generics.ListAPIView):
    queryset = SummaryDescriptionModel.objects.all()
    serializer_class = SummaryDescriptionSerializer

class SummaryDescriptionCreateView(generics.CreateAPIView):
    queryset = SummaryDescriptionModel.objects.all()
    serializer_class = SummaryDescriptionSerializer

class SummaryDescriptionRetrieveView(generics.RetrieveAPIView):
    queryset = SummaryDescriptionModel.objects.all()
    serializer_class = SummaryDescriptionSerializer

class SummaryDescriptionUpdateView(generics.UpdateAPIView):
    queryset = SummaryDescriptionModel.objects.all()
    serializer_class = SummaryDescriptionSerializer

class SummaryDescriptionDestroyView(generics.DestroyAPIView):
    queryset = SummaryDescriptionModel.objects.all()
    serializer_class = SummaryDescriptionSerializer





class BrandListView(generics.ListAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer

class BrandCreateView(generics.CreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer

class BrandRetrieveView(generics.RetrieveAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer

class BrandUpdateView(generics.UpdateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer

class BrandDestroyView(generics.DestroyAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer





class CategoryListView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryDestroyView(generics.DestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer





class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategoryModelSerializer

class SubCategoryCreateView(generics.CreateAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategoryModelSerializer

class SubCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategoryModelSerializer

class SubCategoryUpdateView(generics.UpdateAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategoryModelSerializer

class SubCategoryDestroyView(generics.DestroyAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategoryModelSerializer





class PhotosListView(generics.ListAPIView):
    queryset = PhotosModel.objects.all()
    serializer_class = PhotosModelSerializer

class PhotosCreateView(generics.CreateAPIView):
    queryset = PhotosModel.objects.all()
    serializer_class = PhotosModelSerializer

class PhotosRetrieveView(generics.RetrieveAPIView):
    queryset = PhotosModel.objects.all()
    serializer_class = PhotosModelSerializer

class PhotosUpdateView(generics.UpdateAPIView):
    queryset = PhotosModel.objects.all()
    serializer_class = PhotosModelSerializer

class PhotosDestroyView(generics.DestroyAPIView):
    queryset = PhotosModel.objects.all()
    serializer_class = PhotosModelSerializer





class VideosListView(generics.ListAPIView):
    queryset = VideosModel.objects.all()
    serializer_class = VideosModelSerializer

class VideosCreateView(generics.CreateAPIView):
    queryset = VideosModel.objects.all()
    serializer_class = VideosModelSerializer

class VideosRetrieveView(generics.RetrieveAPIView):
    queryset = VideosModel.objects.all()
    serializer_class = VideosModelSerializer

class VideosUpdateView(generics.UpdateAPIView):
    queryset = VideosModel.objects.all()
    serializer_class = VideosModelSerializer

class VideosDestroyView(generics.DestroyAPIView):
    queryset = VideosModel.objects.all()
    serializer_class = VideosModelSerializer





class ShowRatingListView(generics.ListAPIView):
    queryset = ShowRatingModel.objects.all()
    serializer_class = ShowRatingModelSerializer

class ShowRatingCreateView(generics.CreateAPIView):
    queryset = ShowRatingModel.objects.all()
    serializer_class = ShowRatingModelSerializer

class ShowRatingRetrieveView(generics.RetrieveAPIView):
    queryset = ShowRatingModel.objects.all()
    serializer_class = ShowRatingModelSerializer

class ShowRatingUpdateView(generics.UpdateAPIView):
    queryset = ShowRatingModel.objects.all()
    serializer_class = ShowRatingModelSerializer

class ShowRatingDestroyView(generics.DestroyAPIView):
    queryset = ShowRatingModel.objects.all()
    serializer_class = ShowRatingModelSerializer





class ReviewListView(generics.ListAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer

class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer

class ReviewUpdateView(generics.UpdateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer

class ReviewDestroyView(generics.DestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer





class InventoryMeterListView(generics.ListAPIView):
    queryset = InventoryMeterModel.objects.all()
    serializer_class = InventoryMeterModelSerializer

class InventoryMeterCreateView(generics.CreateAPIView):
    queryset = InventoryMeterModel.objects.all()
    serializer_class = InventoryMeterModelSerializer

class InventoryMeterRetrieveView(generics.RetrieveAPIView):
    queryset = InventoryMeterModel.objects.all()
    serializer_class = InventoryMeterModelSerializer

class InventoryMeterUpdateView(generics.UpdateAPIView):
    queryset = InventoryMeterModel.objects.all()
    serializer_class = InventoryMeterModelSerializer

class InventoryMeterDestroyView(generics.DestroyAPIView):
    queryset = InventoryMeterModel.objects.all()
    serializer_class = InventoryMeterModelSerializer





class Option1ListView(generics.ListAPIView):
    queryset = Option1Model.objects.all()
    serializer_class = Option1ModelSerializer

class Option1CreateView(generics.CreateAPIView):
    queryset = Option1Model.objects.all()
    serializer_class = Option1ModelSerializer

class Option1RetrieveView(generics.RetrieveAPIView):
    queryset = Option1Model.objects.all()
    serializer_class = Option1ModelSerializer

class Option1UpdateView(generics.UpdateAPIView):
    queryset = Option1Model.objects.all()
    serializer_class = Option1ModelSerializer

class Option1DestroyView(generics.DestroyAPIView):
    queryset = Option1Model.objects.all()
    serializer_class = Option1ModelSerializer





class Option2ListView(generics.ListAPIView):
    queryset = Option2Model.objects.all()
    serializer_class = Option2ModelSerializer

class Option2CreateView(generics.CreateAPIView):
    queryset = Option2Model.objects.all()
    serializer_class = Option2ModelSerializer

class Option2RetrieveView(generics.RetrieveAPIView):
    queryset = Option2Model.objects.all()
    serializer_class = Option2ModelSerializer

class Option2UpdateView(generics.UpdateAPIView):
    queryset = Option2Model.objects.all()
    serializer_class = Option2ModelSerializer

class Option2DestroyView(generics.DestroyAPIView):
    queryset = Option2Model.objects.all()
    serializer_class = Option2ModelSerializer





class TagsListView(generics.ListAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagsModelSerializer

class TagsCreateView(generics.CreateAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagsModelSerializer

class TagsRetrieveView(generics.RetrieveAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagsModelSerializer

class TagsUpdateView(generics.UpdateAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagsModelSerializer

class TagsDestroyView(generics.DestroyAPIView):
    queryset = TagsModel.objects.all()
    serializer_class = TagsModelSerializer





class DescriptionListView(generics.ListAPIView):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer

class DescriptionCreateView(generics.CreateAPIView):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer

class DescriptionRetrieveView(generics.RetrieveAPIView):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer

class DescriptionUpdateView(generics.UpdateAPIView):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer

class DescriptionDestroyView(generics.DestroyAPIView):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer