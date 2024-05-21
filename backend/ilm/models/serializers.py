from rest_framework import serializers
from . import Course, Module, Content


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.

    This serializer converts Course model instances into JSON format and 
    validates incoming data for creating or updating Course instances.

    Fields:
        All fields of the Course model are included.
    """
    class Meta:
        model = Course
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Module model.

    This serializer converts Module model instances into JSON format and 
    validates incoming data for creating or updating Module instances.

    Fields:
        All fields of the Module model are included.
    """
    class Meta:
        model = Module
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Content model.

    This serializer converts Content model instances into JSON format and 
    validates incoming data for creating or updating Content instances.

    Fields:
        All fields of the Content model are included.
    """
    class Meta:
        model = Content
        fields = '__all__'
