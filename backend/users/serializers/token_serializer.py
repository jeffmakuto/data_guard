from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token obtain pair serializer.
    """
    default_error_messages = {
        'invalid_credentials': 'Unable to log in with provided credentials.'
    }

    def validate(self, attrs):
        """
        Customizes the token validation process to include user data.
        """
        try:
            data = super().validate(attrs)
        except InvalidToken:
            # If an invalid token is provided, raise a validation error
            raise serializers.ValidationError(
                self.error_messages['invalid_credentials'],
                code='invalid_credentials'
            )

        # Add user data to the response
        data['user'] = UserSerializer(self.user).data
        return data
