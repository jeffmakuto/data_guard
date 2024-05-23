from rest_framework import viewsets
from mod.models import Notification
from mod.serializers.notification_serializer import NotificationSerializer
from mod.permissions.permissions import IsAdminOrReadOnly

class NotificationViewSet(viewsets.ModelViewSet):
    """Notification viewset implementation"""
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminOrReadOnly]

