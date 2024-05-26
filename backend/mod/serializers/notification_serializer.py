from rest_framework import serializers
from mod.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'title', 'message', 'read', 'created_at']
        read_only_fields = ['user', 'created_at']
