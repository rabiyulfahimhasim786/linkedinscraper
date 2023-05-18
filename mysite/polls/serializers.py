from rest_framework import serializers
from .models import Linkedindata

class Linkedindataserializers(serializers.ModelSerializer):
    class Meta:
        model = Linkedindata
        fields = '__all__'