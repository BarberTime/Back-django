from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from apps.usuario_rol.models import UsuarioRol
from apps.rol.models import Rol

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'is_staff']
        read_only_fields = ['date_joined', 'is_staff']

class UsuarioDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'is_staff', 'password']
        read_only_fields = ['date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class LoginSerializer(serializers.Serializer):
    """Serializer para el inicio de sesión de usuarios"""
    username = serializers.CharField(label='Nombre de usuario')
    password = serializers.CharField(write_only=True, label='Contraseña')

    def validate(self, data):
        """Valida las credenciales del usuario"""
        user = authenticate(
            username=data.get('username'),
            password=data.get('password')
        )
        if user and user.is_active:
            return user
        raise serializers.ValidationError({
            'error': 'Credenciales inválidas'
        })

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    is_barbero = serializers.BooleanField(default=False)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            
            # Crear el rol para el usuario
            rol_nombre = 'Barbero' if validated_data['is_barbero'] else 'Cliente'
            rol, created = Rol.objects.get_or_create(nombre=rol_nombre)
            UsuarioRol.objects.create(
                usuario=user,
                rol=rol
            )
            
            return user
        except Exception as e:
            raise serializers.ValidationError({
                'error': f'Error inesperado: {str(e)}'
            })
            
            
            
            return user
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Error al crear el usuario")
        except Exception as e:
            raise serializers.ValidationError(f"Error inesperado: {str(e)}")
    
    def to_representation(self, instance):
        try:
            # Devolver los datos del usuario con su rol
            usuario_rol = UsuarioRol.objects.filter(usuario=instance).first()
            return {
                'id': instance.id,
                'username': instance.username,
                'email': instance.email,
                'rol': usuario_rol.rol.nombre if usuario_rol else None
            }
        except Exception as e:
            raise serializers.ValidationError(f"Error al obtener los datos del usuario: {str(e)}")