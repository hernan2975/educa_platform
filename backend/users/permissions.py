from rest_framework import permissions

class IsPremiumUser(permissions.BasePermission):
    """
    Permiso que restringe el acceso solo a usuarios autenticados con cuenta premium.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_premium
        )

