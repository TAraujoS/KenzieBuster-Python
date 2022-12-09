from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb


class isAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class isAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated and (
            request.user == obj or request.user.is_superuser
        ):
            return True

        return False
