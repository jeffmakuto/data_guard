from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .modules import Module


class Content(models.Model):
    """
    Represents content within a module.
    
    Attributes:
        module (ForeignKey): Foreign key to the associated Module model
        title (str): Title of the content
        content_type (str): Type of content (e.g., document, audio, video, picture)
        file (FileField): File field to store the content file
    """
    CONTENT_TYPES = (
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('picture', 'Picture'),
    )
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    file = models.FileField(upload_to='module_contents/', validators=[FileExtensionValidator(allowed_extensions=['mp3', 'mp4', 'mov', 'avi', 'jpg', 'jpeg', 'png'])])

    def __str__(self):
        """
        Returns a string representation of the content.
        """
        return f"{self.title} ({self.content_type})"

    def clean(self):
        """
        Additional validation logic.
        """
        # Check if title is not blank
        if not self.title:
            raise ValidationError('The title field cannot be blank.')
