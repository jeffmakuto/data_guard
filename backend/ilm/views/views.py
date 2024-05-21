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
    Viewset for Course model.
    Provides CRUD operations for Course objects.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    """
    Viewset for Module model.
    Provides CRUD operations for Module objects.
    """
    queryset = Module.objects.all().select_related('course')
    serializer_class = ModuleSerializer


class ContentViewSet(viewsets.ModelViewSet):
    """
    Viewset for Content model.
    Provides CRUD operations for Content objects.
    """
    queryset = Content.objects.all().select_related('module')
    serializer_class = ContentSerializer
