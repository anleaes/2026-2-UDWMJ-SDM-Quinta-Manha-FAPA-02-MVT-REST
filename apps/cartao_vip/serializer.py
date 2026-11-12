from rest_framework import serializers
from .models import Cartao_Vip

class Cartao_VipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao_Vip 
        fields = '__all__'