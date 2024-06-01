# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from users.serializers import RegisterSerializer
import re
from django.conf import settings


class RegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def is_valid_email_domain(self, email):
        # Retrieve the list of valid email domains from settings
        valid_domains = settings.VALID_EMAIL_DOMAINS

        # Extract domain from email address
        domain = re.search("@[\w.]+", email).group()

        # Check if domain is in the list of valid domains
        if domain[1:] in valid_domains:
            return True
        return False

    def post(self, request, *args, **kwargs):
        # Check if email already exists
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if username already exists
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate password strength
        password = request.data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

        # Validate email domain
        if not self.is_valid_email_domain(email):
            return Response({'error': 'Invalid email domain.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
