from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import SET_NULL
from users.models import User
from categorias.models import Categorias

# Create your models here.
def path_to_tareas(instance, filename):                   # new
    return f'tareas/{instance.id}/{filename}'

class Tareas(models.Model):
    titulo=models.CharField(max_length=255)
    contenido=models.TextField(max_length=5000)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(
        upload_to=path_to_tareas, null=True, blank=True)
    tarea_activa = models.BooleanField(default=False)
    tarea_pospuesta = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Tareas, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
