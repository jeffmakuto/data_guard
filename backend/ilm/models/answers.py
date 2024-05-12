from django.db import models
from ilm.models.questions import Question
from django.core.exceptions import ValidationError


class AnswerOption(models.Model):
    """
    Represents an option for a question.
    """
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    order = models.IntegerField(blank=True, null=True)  # Optional field for ordering options

    def clean(self):
        """
        Ensure the answer text is unique among options for the associated question.
        """
        if self.question.options.filter(text=self.text).exists():
            raise ValidationError(f"Duplicate answer option: {self.text}")

    def __str__(self):
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

    def clean(self):
        """
        Ensure the answer text matches one of the options for the associated question.
        """
        if not self.question.options.filter(text=self.text).exists():
            raise ValidationError(f"{self.text} is not a valid option for the question.")

    def save(self, *args, **kwargs):
        """
        Override the save method to perform validation before saving.
        """
        self.full_clean()  # Validate the answer before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Answer to '{self.question.text}': {self.text} (Correct: {self.is_correct})"
