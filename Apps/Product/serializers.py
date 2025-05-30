from rest_framework import serializers
from .models import (
    DetailModel, SummaryDescriptionModel, BrandModel,

)





class DetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailModel
        fields = '__all__'





class SummaryDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryDescriptionModel
        fields = '__all__'





class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'