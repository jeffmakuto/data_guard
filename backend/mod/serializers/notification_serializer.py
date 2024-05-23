from rest_framework import serializers
from mod.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def validate_title(self, value: str) -> str:
        """Validate the title field"""
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return value