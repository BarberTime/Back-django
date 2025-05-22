from .models import ImagenesNegocio
from .serializers import ImagenesNegocioSerializer, ImagenesNegocioDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ImagenesNegocioList(generics.ListCreateAPIView):
    queryset = ImagenesNegocio.objects.all()
    serializer_class = ImagenesNegocioSerializer
    permission_classes = [IsAuthenticated]

class ImagenesNegocioDetail(generics.RetrieveAPIView):
    queryset = ImagenesNegocio.objects.all()
    serializer_class = ImagenesNegocioDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_imagen'

class ImagenesNegocioUpdate(generics.UpdateAPIView):
    queryset = ImagenesNegocio.objects.all()
    serializer_class = ImagenesNegocioDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_imagen'

class ImagenesNegocioDelete(generics.DestroyAPIView):
    queryset = ImagenesNegocio.objects.all()
    serializer_class = ImagenesNegocioSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_imagen'