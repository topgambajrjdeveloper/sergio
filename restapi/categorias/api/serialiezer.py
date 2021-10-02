from rest_framework.serializers import ModelSerializer
from categorias.models import Categorias
from users.api.serialiezer import UserProfileTareasComentariosSerializer

class CategoriasSerializer(ModelSerializer):
    user = UserProfileTareasComentariosSerializer()
    class Meta:
        model = Categorias
        fields = [
            'titulo',
            'slug',
            'image',
            'publicado',
            'user'
        ]


class CategoriasTareasComentariosSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = [
            'titulo',
        ]
