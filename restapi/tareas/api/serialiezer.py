from rest_framework.serializers import ModelSerializer
from tareas.models import Tareas
from users.api.serialiezer import UserProfileTareasComentariosSerializer
from categorias.api.serialiezer import CategoriasTareasComentariosSerializer


class TareasSerializer(ModelSerializer):
    user = UserProfileTareasComentariosSerializer()
    categoria = CategoriasTareasComentariosSerializer()
    class Meta:
        model = Tareas
        fields = [
            'titulo',
            'contenido',
            'slug',
            'image',
            'tarea_activa',
            'tarea_pospuesta',
            'user', 'categoria',
        ]
