from rest_framework import serializers
from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id_servicio', 'nombre', 'categoria', 'precio', 'descripcion', 'imagen', 'fecha_registro']
        read_only_fields = ['id_servicio', 'fecha_registro']

class ServicioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id_servicio', 'nombre', 'categoria', 'precio', 'descripcion', 'imagen', 'fecha_registro']
        read_only_fields = ['id_servicio', 'fecha_registro']