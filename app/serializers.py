from dataclasses import field
from pyexpat import model
from .models import Suscripcion, Tipo_sub
from rest_framework import serializers

class Tipo_subSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_sub
        fields = '__all__'

class SuscripcionSerializer(serializers.ModelSerializer):
    tipo =  Tipo_subSerializer(read_only=True)
    class Meta:
        model = Suscripcion
        fields = '__all__'