from rest_framework import serializers
from . import Course, Module, Content


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.
    """
    class Meta:
        model = Course
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Module model.
    Includes nested serializer for the related Course.
    """
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Module
        fields = '__all__'


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
