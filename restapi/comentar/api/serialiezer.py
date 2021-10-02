from rest_framework.serializers import ModelSerializer
from comentar.models import Comentar
from users.api.serialiezer import UserProfileTareasComentariosSerializer
from categorias.api.serialiezer import CategoriasTareasComentariosSerializer


class ComentarSerializer(ModelSerializer):
    user = UserProfileTareasComentariosSerializer()
    categoria = CategoriasTareasComentariosSerializer()
    class Meta:
        model = Comentar
        fields = [
            'comentarios',            
            'user', 
        ]
