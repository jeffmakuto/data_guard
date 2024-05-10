from django.db import models


class Course(models.Model):
    """
    Represents a course within the learning platform.
    
    Attributes:
        title (str): Title of the course
        description (str): Description of the course
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the title
        and description.
        """
        return f"{self.title}: {self.description}"
