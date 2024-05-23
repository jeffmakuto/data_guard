from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import UserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token obtain pair serializer.
    """
    def validate(self, attrs):
        """
        Customizes the token validation process to include user data.
        """
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data