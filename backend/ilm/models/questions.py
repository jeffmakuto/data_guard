from django.db import models
from ilm.models.quiz import Quiz


class Question(models.Model):
  """
  Represents a question within a quiz
  """
  quiz = models.ForeignKey(
    Quiz, on_delete=models.CASCADE
  )
  text = models.TextField(blank=True, null=True)
  correct_answer = models.ForeignKey(
    AnswerOption, on_delete=models.CASCADE, related_name="questions"
  )
  answers = models.ManyToManyField(AnswerOption)

  def __str__(self) -> str:
    """
    Return a string representation
    """
    return self.text
  
