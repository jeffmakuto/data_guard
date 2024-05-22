from rest_framework import serializers
from ilm.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.
    """
    class Meta:
        model = Course
        fields = '__all__'
