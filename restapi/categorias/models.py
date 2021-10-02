from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import SET_NULL
from users.models import User
# Create your models here.
def path_to_categorias(instance, filename):                   # new
    return f'categorias/{instance.id}/{filename}'

class Categorias(models.Model):
    titulo=models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to=path_to_categorias, null=True, blank=True)
    publicado=models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Categorias, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
