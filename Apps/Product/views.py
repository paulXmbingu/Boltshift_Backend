from rest_framework import generics
from .models import (
    DetailModel, 
    )
from .serializers import (
    DetailModelSerializer, 
    )




'''DETAIL VIEWS'''
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