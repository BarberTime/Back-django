from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Plan, Suscripcion
from .serializers import PlanSerializer, SuscripcionSerializer
from apps.negocio.models import Negocio
class PlanListCreateView(generics.ListCreateAPIView):
    queryset = Plan.objects.filter(activo=True)
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo mostrar planes activos
        return self.queryset.filter(activo=True)

class PlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        # Solo permitir ver/actualizar planes activos
        return self.queryset.filter(activo=True)

class SuscripcionListCreateView(generics.ListCreateAPIView):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo mostrar las suscripciones del negocio actual
        negocio = Negocio.objects.get(propietario=self.request.user)
        return self.queryset.filter(negocio=negocio)

    def perform_create(self, serializer):
        # Obtener el negocio del usuario actual
        negocio = Negocio.objects.get(propietario=self.request.user)
        serializer.save(negocio=negocio)

class SuscripcionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        # Solo permitir ver/actualizar las suscripciones del negocio actual
        negocio = Negocio.objects.get(propietario=self.request.user)
        return self.queryset.filter(negocio=negocio)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.esta_activa():
            return Response({'error': 'Esta suscripción está inactiva'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.esta_activa():
            return Response({'error': 'Esta suscripción está inactiva'}, status=status.HTTP_403_FORBIDDEN)
        instance.estado = 'CANCELADA'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
