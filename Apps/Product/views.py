from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from .models import (
    DetailModel,
    )
from .serializers import (
    DetailModelSerializer,
    )





class DetailModelListView(ListAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailModelCreateView(CreateAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailModelRetrieveView(RetrieveAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailModelUpdateView(UpdateAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer

class DetailModelDestroyView(DestroyAPIView):
    queryset = DetailModel.objects.all()
    serializer_class = DetailModelSerializer