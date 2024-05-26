from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    """Notification class"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=225)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.message}"

    class Meta:
        app_label = 'mod'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['read']),
        ]
