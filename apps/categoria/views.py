from .models import Categoria
from .serializers import CategoriaSerializer, CategoriaDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class CategoriaDetail(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_categoria'

class CategoriaUpdate(generics.UpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_categoria'

class CategoriaDelete(generics.DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_categoria'


    


