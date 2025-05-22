from rest_framework import serializers
from .models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol', 'nombre']
        read_only_fields = ['id_rol']

class RolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol', 'nombre']
        read_only_fields = ['id_rol']
