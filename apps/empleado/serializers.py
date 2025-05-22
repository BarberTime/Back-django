# apps/empleado/serializers.py
from rest_framework import serializers
from .models import Empleado
from apps.usuario.serializers import UsuarioSerializer
from apps.rol.serializers import RolSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    rol = RolSerializer(read_only=True)
    
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'usuario', 'negocio', 'rol', 'especialidad', 'experiencia_anios', 'foto_perfil', 'fecha_contratacion', 'activo']
        read_only_fields = ['id_empleado', 'fecha_contratacion', 'rol']
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = User.objects.create_user(**usuario_data)
        empleado = Empleado.objects.create(
            usuario=usuario,
            negocio=validated_data['negocio'],
            especialidad=validated_data['especialidad'],
            experiencia_anios=validated_data['experiencia_anios']
        )
        return empleado

class SubirFotoPerfilSerializer(serializers.Serializer):
    foto_perfil = serializers.ImageField(required=True)
    
    def save(self, empleado_id):
        empleado = Empleado.objects.get(id_empleado=empleado_id)
        empleado.foto_perfil = self.validated_data['foto_perfil']
        empleado.save()
        return empleado

class EliminarFotoPerfilSerializer(serializers.Serializer):
    def save(self, empleado_id):
        empleado = Empleado.objects.get(id_empleado=empleado_id)
        empleado.foto_perfil = None
        empleado.save()
        return empleado