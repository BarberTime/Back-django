from .models import Negocio
from .serializers import NegocioSerializer, NegocioDetailSerializer
from rest_framework import generics, status
from rest_framework.response import Response

class NegocioList(generics.ListCreateAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

class NegocioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioDetailSerializer
    lookup_field = 'id_negocio'

class NegocioUpdate(generics.UpdateAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
    lookup_field = 'id_negocio'

class NegocioDelete(generics.DestroyAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
    lookup_field = 'id_negocio'

class NegocioPublicoList(generics.ListAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioDetailSerializer
    permission_classes = []