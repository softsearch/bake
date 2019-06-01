from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
        Object-level permission to only allow owners of an object to edit it.
        Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            # Only admin can delete. 
            return request.user.is_superuser

        return obj.user == request.user or request.user.is_superuser
