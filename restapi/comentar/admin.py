from django.contrib import admin
from comentar.models import Comentar
# Register your models here.


@admin.register(Comentar)
class ComentarAdmin(admin.ModelAdmin):
    list_display = ["comentario", "user"]
