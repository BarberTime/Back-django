from .models import Rol
from .serializers import RolSerializer, RolDetailSerializer
from rest_framework import generics

class RolList(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetail(generics.RetrieveAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolDetailSerializer
    lookup_field = 'id_rol'

class RolUpdate(generics.UpdateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolDetailSerializer
    lookup_field = 'id_rol'

class RolDelete(generics.DestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    lookup_field = 'id_rol'
