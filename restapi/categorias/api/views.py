from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from categorias.models import Categorias
from categorias.api.serialiezer import CategoriasSerializer
from categorias.api.permission import IsOwnerOrReadAndCreateOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CategoriasSerializer
    queryset=Categorias.objects.all()
    """Buscar por la propiedad slug"""
    lookup_field='slug'
    """Devolver las categorias publicadas"""
    # queryset = Categorias.objects.filter()
    """"Filtro de rest_framework"""
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo']
