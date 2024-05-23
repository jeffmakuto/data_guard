from rest_framework import serializers
from ilm.models import Content


class ContentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Content model.
    """
    class Meta:
        model = Content
        fields = '__all__'

    def validate_title(self, value: str) -> str:
        """
        Validates the title field to ensure it is not blank.
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value
