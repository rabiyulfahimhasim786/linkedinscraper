from rest_framework import serializers
from .models import Simplehireddata

class Simplehireddataserializers(serializers.ModelSerializer):
    class Meta:
        model = Simplehireddata
        fields = '__all__'