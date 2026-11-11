from .models import Espectador
from rest_framework import serializers

class EspectadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espectador
        fields = '__all__'