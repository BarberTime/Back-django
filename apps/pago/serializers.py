from rest_framework import serializers
from .models import Pago    

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id_pago', 'reserva', 'metodo_pago', 'fecha_pago']
        read_only_fields = ['id_pago', 'fecha_pago']

class PagoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id_pago', 'reserva', 'metodo_pago', 'fecha_pago']
        read_only_fields = ['id_pago', 'fecha_pago']