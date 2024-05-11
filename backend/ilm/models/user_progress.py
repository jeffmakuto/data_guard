from django.db import models
from django.contrib.auth.models import User
from ilm.models.quiz import Quiz


class UserProgress(models.Model):
  """
  Represents user progress within the quiz.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  is_completed = models.BooleanField(default=False)
  score = models.IntegerField()

  def __str__(self) -> str:
    """
    Returns a string representation.
    """
    user_info = f"User: {self.user.username}"
    quiz_info = f"Quiz: {self.quiz.title}, Score: {self.score}"
    return user_info + "\n" + quiz_info
