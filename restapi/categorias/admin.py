from django.contrib import admin
from categorias.models import Categorias

# Register your models here.
@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["titulo", "user", "image", "publicado"]
    
