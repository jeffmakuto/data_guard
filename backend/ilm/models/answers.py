from django.db import models
from django.core.exceptions import ValidationError
from ilm.models.questions import Question


class Answer(models.Model):
    """
    Represents an answer to a question.
    """
    question = models.ForeignKey(
      Question, related_name='answers', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField()

    OPTIONS = {
        'A': 'Option A',
        'B': 'Option B',
        'C': 'Option C',
    }

    # Use choices field with the dictionary
    text = models.CharField(max_length=100, choices=OPTIONS.items())

    def clean(self):
        """
        No custom validation needed as choices field handles it
        """
        pass

    def save(self, *args, **kwargs):
        """
        Override the save method to perform validation before saving.
        """
        self.full_clean()  # Validate the answer before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Answer to '{self.question.text}': {self.text} (Correct: {self.is_correct})"
