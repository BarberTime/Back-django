from .models import Pago
from .serializers import PagoSerializer, PagoDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class PagoList(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]

class PagoDetail(generics.RetrieveAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_pago'

class PagoUpdate(generics.UpdateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_pago'

class PagoDelete(generics.DestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_pago'