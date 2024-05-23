from rest_framework import viewsets
from ilm.models import Course
from ilm.serializers import CourseSerializer
from ilm.permissions.permissions import IsAdminOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    """
    Viewset for Course model.
    Provides CRUD operations for Course objects.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
