from rest_framework.permissions import BasePermission


# Solo los is_staff podran hacer el CRUD completo de las categorias
class IsAdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return False
