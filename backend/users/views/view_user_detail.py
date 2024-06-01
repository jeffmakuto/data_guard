from rest_framework import generics, permissions
from django.contrib.auth.models import User
from serializers import UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Endpoint for retrieving and updating user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Returns the current authenticated user.
        """
        return self.request.user
