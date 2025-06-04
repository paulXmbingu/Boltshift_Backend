from rest_framework import generics
from .models import (
    DetailModel, 
    )
from .serializers import (
    DetailModelSerializer, 
    )





class DetailListView(generics.ListAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

