from django.db import models
from .courses import Course


class Module(models.Model):
    """
    Represents a module within a course.

    Attributes:
        course (ForeignKey): Foreign key to the associated Course model
        title (str): Title of the module
        description (str): Description of the module (optional)
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation.
        """
        return f"{self.title} (Course: {self.course.title})"