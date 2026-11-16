from .models import Sede
from rest_framework import serializers

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
            model = Sede
            fields = '__all__'


