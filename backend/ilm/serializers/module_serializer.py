from rest_framework import serializers
from models import Module
from . import CourseSerializer


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Module model.
    Includes nested serializer for the related Course.
    """
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Module
        fields = '__all__'
