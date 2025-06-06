from rest_framework import generics
from .models import (
    DetailModel, SummaryDescriptionModel, BrandModel
    )
from .serializers import (
    DetailModelSerializer, SummaryDescriptionSerializer, BrandModelSerializer
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
    