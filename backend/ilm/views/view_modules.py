from rest_framework import viewsets
from ilm.models import Module
from ilm.serializers import ModuleSerializer
from ilm.permissions.permissions import IsAdminOrReadOnly


class ModuleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for Module model.
    Provides CRUD operations for Module objects.
    """
    queryset = Module.objects.all().select_related('course')
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminOrReadOnly]
