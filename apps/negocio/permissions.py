from rest_framework import permissions
from apps.usuario_rol.models import UsuarioRol

class EsBarberoPermission(permissions.BasePermission):
    """Permiso para verificar que el usuario es un Barbero"""
    
    def has_permission(self, request, view):
        """Verifica si el usuario tiene el rol de Barbero"""
        try:
            usuario_rol = UsuarioRol.objects.get(usuario=request.user)
            return usuario_rol.rol.nombre == 'Barbero'
        except UsuarioRol.DoesNotExist:
            return False
