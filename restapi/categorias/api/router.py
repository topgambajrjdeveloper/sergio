from rest_framework.routers import DefaultRouter
from categorias.api.views import CategoryApiViewSet


router_categorias =DefaultRouter()
router_categorias.register(
    prefix='categorias', basename='categorias', viewset=CategoryApiViewSet)
