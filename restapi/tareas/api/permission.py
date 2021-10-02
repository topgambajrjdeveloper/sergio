from rest_framework.permissions import BasePermission

from tareas.models import Tareas


# Solo los is_staff podran hacer el CRUD completo de las tareas
class IsAdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return False


#Todo pueden leer y cree, pero el creador del tarea puede hacer el CRUD completo
class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_tarea = view.kwargs['pk']
            tarea = Tareas.objects.get(pk=id_tarea)

            id_user = request.user.pk
            id_user_tarea = tarea.user_id
            if id_user == id_user_tarea:
                return True
            return False
