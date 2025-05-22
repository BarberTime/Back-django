from .models import Horario
from .serializers import HorarioSerializer, HorarioDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class HorarioList(generics.ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]

class HorarioDetail(generics.RetrieveAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_horario'

class HorarioUpdate(generics.UpdateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_horario'

class HorarioDelete(generics.DestroyAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_horario'

