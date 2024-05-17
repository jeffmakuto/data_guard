from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from .modules import Module


class Content(models.Model):
    """
    Represents content.
    """
    TYPE_CHOICES = (
        ('document', 'Document'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(1000)])
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=False)
    file_path = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        """
        Returns a string representation of the content object.
        """
        info = f"Title: {self.title} : {self.description or 'No description'}"
        details = f"Type: {self.get_type_display()} \nFile Path: {self.file_path}"
        return info + "\n" + details

    def clean(self):
        """
        Additional validation logic.
        """
        if not self.title:
            raise ValidationError('The title field cannot be blank.')

        if self.description and len(self.description) > 1000:
            raise ValidationError('The description cannot be longer than 1000 characters.')

        if not self.type:
            raise ValidationError('The type field cannot be blank.')

        if not self.file_path:
            raise ValidationError('The file path cannot be blank.')
