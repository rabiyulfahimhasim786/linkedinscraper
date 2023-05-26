from rest_framework import serializers
from .models import Barcodefile

class Barcodefileserializers(serializers.ModelSerializer):
    class Meta:
        model = Barcodefile
        fields = '__all__'