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

    def validate_content_type(self, value: str) -> str:
        """
        Validates the content_type field to ensure it is one of the allowed choices.
        """
        allowed_content_types = ['audio', 'picture', 'video']
        if value not in allowed_content_types:
            raise serializers.ValidationError("Invalid content type.")
        return value

    def validate_file(self, value) -> str:
        """
        Validates the uploaded file based on the selected content type.
        """
        content_type = self.initial_data.get('content_type')
        if not content_type:
            raise serializers.ValidationError("Content type is required.")

        # Check file extension based on content type
        if content_type == 'audio' and not value.name.lower().endswith('.mp3'):
            raise serializers.ValidationError("Invalid file format for audio content. Please upload an MP3 file.")
        elif content_type == 'picture' and not value.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            raise serializers.ValidationError("Invalid file format for picture content. Please upload a JPG, JPEG, or PNG file.")
        elif content_type == 'video' and not value.name.lower().endswith(('.mp4', '.mov', '.avi')):
            raise serializers.ValidationError("Invalid file format for video content. Please upload an MP4, MOV, or AVI file.")

        return value
