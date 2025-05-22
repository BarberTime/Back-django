# apps/empleado/views.py
from .models import Empleado
from .serializers import EmpleadoSerializer, SubirFotoPerfilSerializer, EliminarFotoPerfilSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate

class EmpleadoList(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(negocio=self.request.user.negocio)

class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'id_empleado'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(negocio=self.request.user.negocio)

class EmpleadoLogin(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user and hasattr(user, 'empleado'):
            empleado = user.empleado
            if empleado.rol.nombre == 'Empleado':
                return Response({
                    'id': empleado.id_empleado,
                    'username': user.username,
                    'especialidad': empleado.especialidad,
                    'negocio': empleado.negocio.nombre,
                    'foto_perfil': empleado.foto_perfil.url if empleado.foto_perfil else None
                })
        return Response({'error': 'Credenciales inválidas'}, status=401)

class SubirFotoPerfil(generics.CreateAPIView):
    serializer_class = SubirFotoPerfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        empleado_id = request.data.get('empleado_id')
        if not empleado_id:
            return Response({'error': 'empleado_id is required'}, status=400)
        
        # Verificar que el empleado pertenece al negocio del usuario actual
        empleado = Empleado.objects.get(id_empleado=empleado_id, negocio__usuario=request.user)
        empleado = serializer.save(empleado_id=empleado_id)
        return Response({'message': 'Foto de perfil subida exitosamente'}, status=201)

class EliminarFotoPerfil(generics.DestroyAPIView):
    serializer_class = EliminarFotoPerfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        empleado_id = request.data.get('empleado_id')
        if not empleado_id:
            return Response({'error': 'empleado_id is required'}, status=400)
        
        # Verificar que el empleado pertenece al negocio del usuario actual
        empleado = Empleado.objects.get(id_empleado=empleado_id, negocio__usuario=request.user)
        serializer = self.get_serializer()
        serializer.save(empleado_id=empleado_id)
        return Response({'message': 'Foto de perfil eliminada exitosamente'}, status=200)