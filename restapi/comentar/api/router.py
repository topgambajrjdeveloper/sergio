from rest_framework.routers import DefaultRouter
from comentar.api.views import ComentarApiViewSet


router_comentar = DefaultRouter()
router_comentar.register(
    prefix='comentarios', basename='comentarios', viewset=ComentarApiViewSet)
