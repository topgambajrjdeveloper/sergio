from rest_framework.permissions import BasePermission

from categorias.api.serialiezer import Categorias



# Solo los is_staff podran hacer el CRUD completo de las categorias
class IsAdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return False

#Todo pueden leer y cree, pero el creador del categoria puede hacer el CRUD completo
class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_categoria = view.kwargs['pk']
            categoria = Categorias.objects.get(pk=id_categoria)

            id_user = request.user.pk
            id_user_categoria = categoria.user_id
            if id_user == id_user_categoria:
                return True
            return False
