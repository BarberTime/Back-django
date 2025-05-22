from .models import Servicio
from .serializers import ServicioSerializer, ServicioDetailSerializer
from rest_framework import generics

class ServicioList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioDetailSerializer
    lookup_field = 'id_servicio'

class ServicioUpdate(generics.UpdateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioDetailSerializer
    lookup_field = 'id_servicio'

class ServicioDelete(generics.DestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_field = 'id_servicio'