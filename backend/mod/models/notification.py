#!/usr/bin/env python

from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    """Notification class"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the intended message notification"""
        return self.message
    
    class Meta:
        app_label = 'mod'