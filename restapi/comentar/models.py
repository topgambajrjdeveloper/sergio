from django.db import models

from users.models import User
from tareas.models import Tareas

# Create your models here.
class Comentar(models.Model):
    comentario=models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tarea = models.ForeignKey(Tareas, on_delete=models.SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "comantar"
        verbose_name_plural = "comentarios"

    def __str__(self):
        return self.comentario
