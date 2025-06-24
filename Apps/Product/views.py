from rest_framework import generics
from .models import (
    DetailModel, SummaryDescriptionModel, BrandModel,
    CategoryModel, SubCategoryModel, PhotosModel, 
    VideosModel, ShowRatingModel, 
)
from .serializers import (
    DetailModelSerializer, SummaryDescriptionSerializer, BrandModelSerializer,
    CategoryModelSerializer, SubCategoryModelSerializer, PhotosModelSerializer,
    VideosModelSerializer, ShowRatingModelSerializer
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
