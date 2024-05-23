from rest_framework import viewsets
from ilm.models import Content
from ilm.serializers import ContentSerializer
from ilm.permissions.permissions import IsAdminOrReadOnly


class ContentViewSet(viewsets.ModelViewSet):
    """
    Viewset for Content model.
    Provides CRUD operations for Content objects.
    """
    queryset = Content.objects.all().select_related('module')
    serializer_class = ContentSerializer
    permission_classes = [IsAdminOrReadOnly]
