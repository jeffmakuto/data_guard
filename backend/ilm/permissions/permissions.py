from rest_framework import permissions
from django.http import HttpRequest


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only administrators to create, update, or delete.
    Read-only access is granted to everyone.
    """
    def has_permission(self, request: HttpRequest, view) -> bool:
        """
        Check if the user has permission to perform the requested action.

        Args:
            request: The incoming request.
            view: The view being accessed.

        Returns:
            bool: True if the request is a safe method or the user is an admin, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff
