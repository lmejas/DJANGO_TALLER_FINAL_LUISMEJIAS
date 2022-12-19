from rest_framework import serializers
from .models import Seminario, Institucion

class SeminarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminario
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'