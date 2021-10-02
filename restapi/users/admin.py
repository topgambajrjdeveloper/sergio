from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # pass
    fieldsets = (
        ('Datos del usuario', {'fields': ('first_name',
         'last_name', 'image', 'email', 'username', 'password')}),
        ('Redes sociales', {'fields': ('facebook', 'instagram', 'twitter', 'website')}),
        ('Permisos', {'fields': ('premium', 'is_active')}),
        ('Controles', {'fields': ('groups', 'user_permissions')})
    )
