from rest_framework import serializers
from .models import Reserva     

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'negocio', 'usuario', 'servicio', 'fecha', 'hora', 'estado', 'fecha_registro']
        read_only_fields = ['id_reserva', 'fecha_registro']

class ReservaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'negocio', 'usuario', 'servicio', 'fecha', 'hora', 'estado', 'fecha_registro']
        read_only_fields = ['id_reserva', 'fecha_registro']