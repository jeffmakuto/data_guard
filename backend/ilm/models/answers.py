from django.db import models
from ilm.models.questions import Question
from django.core.exceptions import ValidationError
from ilm.models.signals import answer_saved, answer_option_saved
from typing import Any


class AnswerOption(models.Model):
    """
    Represents an option for a question.
    """
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    order = models.IntegerField(blank=True, null=True)  # Optional field for ordering options

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Save method overridden to send a signal after saving the instance.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
            
        Returns:
            None
        """
        super().save(*args, **kwargs)
        answer_option_saved.send(
            sender=self.__class__, instance=self
        )

    def __str__(self):
        """
        Returns a string representation
        """
        return f"Option for '{self.question.text}': {self.text}"


class Answer(models.Model):
    """
    Represents an answer to a question.
    """
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField()

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Override the save method to perform validation before saving.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().save(*args, **kwargs)
        answer_saved.send(
            sender=self.__class__, instance=self
        )  # Send signal after save


    def __str__(self):
        """
        Returns a string representation
        """
        return f"Answer to '{self.question.text}': {self.text} (Correct: {self.is_correct})"
