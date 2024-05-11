from django.db import models


class Quiz(models.Model):
  """
  Represents a quiz
  """
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)

  def __str__(self) -> str:
    """
    Return a string representation of the quiz
    """
    return f"{title}: {description}"
