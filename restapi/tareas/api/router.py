from rest_framework.routers import DefaultRouter
from tareas.api.views import TareasApiViewSet


router_tareas = DefaultRouter()
router_tareas.register(
    prefix='tareas', basename='tareas', viewset=TareasApiViewSet)
