from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from . import Module
from ilm.validators import MaxFileSizeValidator


class Content(models.Model):
    """
    Represents content within a module.

    Attributes:
        module (ForeignKey): Foreign key to the associated Module model
        title (str): Title of the content
        content_type (str): Type of content (
        e.g., document, audio, video, picture
        )
        file (FileField): File field to store the content file
    """
    CONTENT_TYPES = (
        ('audio', 'Audio'),
        ('picture', 'Picture'),
        ('video', 'Video'),
    )

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    file = models.FileField(
        upload_to='module_contents/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'mp3', 'mp4', 'mov', 'avi', 'jpg', 'jpeg', 'png'
                ]
            ),
            MaxFileSizeValidator(100 * 1024 * 1024)  # 100 MB limit
        ]
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the content.
        """
        return f"{self.title} ({self.content_type})"

    class Meta:
        """
        Meta class to define model-specific options.
        """
        # Enforce uniqueness of title within the same module
        unique_together = ['module', 'title']
