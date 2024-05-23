from rest_framework import generics, permissions
from django.contrib.auth.models import User
from serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
