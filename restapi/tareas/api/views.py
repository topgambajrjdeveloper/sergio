from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from tareas.models import Tareas
from tareas.api.serialiezer import TareasSerializer
from tareas.api.permission import IsOwnerOrReadAndCreateOnly
from django_filters.rest_framework import DjangoFilterBackend


class TareasApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = TareasSerializer
    queryset = Tareas.objects.all()
    """Buscar por la propiedad slug"""
    lookup_field = 'slug'
    """Devolver las categorias publicadas"""
    # queryset = Tareas.objects.filter()
    """"Filtro de rest_framework"""
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria']
