
from .models import UsuarioRol
from .serializers import UsuarioRolSerializer, UsuarioRolDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UsuarioRolList(generics.ListCreateAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer
    permission_classes = [IsAuthenticated]

class UsuarioRolDetail(generics.RetrieveAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_usuario_rol'

class UsuarioRolUpdate(generics.UpdateAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_usuario_rol'

class UsuarioRolDelete(generics.DestroyAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_usuario_rol'

