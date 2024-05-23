from rest_framework import permissions
from django.http import HttpRequest


class IsAdminOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow admins to edit objects"""

    def has_permission(self, request: HttpRequest, view) -> bool:
        """Check if user has permission to perform the action"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff