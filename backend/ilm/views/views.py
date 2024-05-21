from rest_framework import viewsets
from models import (
    Course,
    Module,
    Content,
    CourseSerializer,
    ModuleSerializer,
    ContentSerializer
)


class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing modules.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ContentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contents.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
