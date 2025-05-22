from rest_framework import serializers
from .models import UsuarioRol  

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = ['id_usuario_rol', 'usuario', 'rol', 'fecha_registro']
        read_only_fields = ['id_usuario_rol', 'fecha_registro']

class UsuarioRolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = ['id_usuario_rol', 'usuario', 'rol', 'fecha_registro']
        read_only_fields = ['id_usuario_rol', 'fecha_registro']