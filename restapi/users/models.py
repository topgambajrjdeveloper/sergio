from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


def path_to_image(instance, filename):                   # new
    return f'image/{instance.id}/{filename}'

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to=path_to_image, null=True, blank=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    premium= models.BooleanField(default=False)
    # Estas dos lineas de debajo son para que se acceda con el email que es único
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.email
    # pass