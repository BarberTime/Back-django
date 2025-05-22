from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import CurrentUserDefault
from .models import Negocio

class NegocioSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    class Meta:
        model = Negocio
        fields = ['id_negocio', 'nombre', 'usuario', 'descripcion', 'departamento', 'direccion', 'telefono', 'logo', 'foto', 'fecha_registro']
        
    def create(self, validated_data):
        usuario = validated_data.pop('usuario', None)
        negocio = Negocio.objects.create(**validated_data)
        if usuario:
            negocio.usuario = usuario
            negocio.save()
        return negocio

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.usuario:
            data['usuario'] = {
                'id': instance.usuario.id,
                'username': instance.usuario.username,
                'email': instance.usuario.email
            }
        return data

from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class NegocioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ['id_negocio', 'nombre','usuario', 'descripcion', 'departamento', 'direccion', 'telefono', 'logo', 'foto', 'fecha_registro']
       

class ImagenSerializer(serializers.Serializer):
    imagen = serializers.ImageField(required=True)
    
    def save(self, negocio_id):
        negocio = Negocio.objects.get(id_negocio=negocio_id)
        negocio.imagen = self.validated_data['imagen']
        negocio.save()
        return negocio

class LogoSerializer(serializers.Serializer):
    logo = serializers.ImageField(required=True)
    
    def save(self, negocio_id):
        negocio = Negocio.objects.get(id_negocio=negocio_id)
        negocio.logo = self.validated_data['logo']
        negocio.save()
        return negocio