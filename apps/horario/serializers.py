from rest_framework import serializers
from .models import Horario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id_horario', 'negocio', 'dia', 'hora_inicio', 'hora_fin']
        read_only_fields = ['id_horario']

class HorarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id_horario', 'negocio', 'dia', 'hora_inicio', 'hora_fin']
        read_only_fields = ['id_horario']
