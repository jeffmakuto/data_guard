#!/usr/bin/env python

from django.db import models
from django.contrib.auth.models import User

class Bucket(models.Model):
    """Bucket model implementation
    Used as a temporary storage tool for user's within the app
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bucket_name = models.CharField(max_length=30)
    bucket_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    