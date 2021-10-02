from rest_framework.serializers import ModelSerializer
from comentar.models import Comentar
from users.api.serialiezer import UserProfileTareasComentariosSerializer


class ComentarSerializer(ModelSerializer):
    user = UserProfileTareasComentariosSerializer()

    class Meta:
        model = Comentar
        fields = [
            'comentario',
            'user',
        ]
