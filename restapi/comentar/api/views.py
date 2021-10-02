from rest_framework.viewsets import ModelViewSet
from comentar.models import Comentar
from comentar.api.serialiezer import ComentarSerializer
from comentar.api.permission import IsOwnerOrReadAndCreateOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class ComentarApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = ComentarSerializer
    queryset = Comentar.objects.all()
    """Devolver las categorias publicadas"""
    # queryset = Tareas.objects.filter()
    """"Filtro de rest_framework"""
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['tarea']
    """Filto Django"""
    ordering = ['-creado']
