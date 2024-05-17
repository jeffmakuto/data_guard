from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError

class Quiz(models.Model):
    """
    Represents a quiz
    """
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(1000)])

    def __str__(self) -> str:
        """
        Return a string representation of the quiz
        """
        return f"{self.title}: {self.description or 'No description'}"

    def clean(self):
        """
        Additional validation logic.
        """
        if not self.title:
            raise ValidationError('The title field cannot be blank.')

        if self.description and len(self.description) > 1000:
            raise ValidationError('The description cannot be longer than 1000 characters.')
