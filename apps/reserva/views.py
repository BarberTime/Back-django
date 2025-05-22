from .models import Reserva
from .serializers import ReservaSerializer, ReservaDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

class ReservaDetail(generics.RetrieveAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_reserva'

class ReservaUpdate(generics.UpdateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_reserva'

class ReservaDelete(generics.DestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_reserva'