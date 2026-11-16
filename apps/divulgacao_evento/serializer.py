from rest_framework import serializers
from .models import Divulgacao_Evento

class Divulgacao_EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divulgacao_Evento 
        fields = '__all__'