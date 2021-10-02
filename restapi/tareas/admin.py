from django.contrib import admin
from tareas.models import Tareas

# Register your models here.
@admin.register(Tareas)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["titulo", "slug", "image", "tarea_activa"]
    search_fields = ["titulo"]
