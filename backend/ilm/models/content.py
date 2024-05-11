from django.db import models


class Content(models.Model):
  """
  Represents content
  """
  TYPE_CHOICES = [
    'document': 'Document',
    'audio': 'Audio',
    'video': 'Video',
  ]

  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  type = models.CharField(
    max_length=20, choices=TYPE_CHOICES.items()
  )
  file_path = models.CharField(max_length=255)

  def __str__(self) -> str:
    """
    Returns a string representation of the content object.
    """
    info = f"Title: {self.title} : {self.description}"
    details = f"Type: {self.TYPE_CHOICES[self.type]} \nFile Path: {self.file_path}"
    return info + details
