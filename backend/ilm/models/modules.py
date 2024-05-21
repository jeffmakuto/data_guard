from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
from . import Course


class Module(models.Model):
    """
    Represents a module within a course.

    Attributes:
        course (ForeignKey): Foreign key to the associated Course model
        title (str): Title of the module
        description (str): Description of the module (optional)
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(
        blank=True, null=True, validators=[MaxLengthValidator(1000)]
    )

    def __str__(self):
        """
        Returns a string representation.
        """
        return f"{self.title} (Course: {self.course.title})"

    def clean(self):
        """
        Additional validation logic.
        """
        if not self.title:
            raise ValidationError('The title field cannot be blank.')

        if self.description and len(self.description) > 1000:
            raise ValidationError(
                'The description cannot be longer than 1000 characters.'
            )
