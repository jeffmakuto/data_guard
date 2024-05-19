from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError


class Course(models.Model):
    """
    Represents a course within the learning platform.
    Attributes:
        title (str): Title of the course
        description (str): Description of the course
    """
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(
        blank=True, null=True, validators=[MaxLengthValidator(1000)]
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the title
        and description.
        """
        return f"{self.title}: {self.description}"

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
