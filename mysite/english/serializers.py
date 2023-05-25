from rest_framework import serializers
from .models import Spellchecker

class Spellcheckerserializers(serializers.ModelSerializer):
    class Meta:
        model = Spellchecker
        fields = ('id', 'inputtext','outputtext')