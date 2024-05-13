from django.apps import apps
from django.db import models
from django.core.exceptions import ValidationError


class AnswerOption(models.Model):
    """
    Represents an option for an answer to a question.
    """
    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('question', 'text')

    def __str__(self):
        return self.text


class Answer(models.Model):
    """
    Represents an answer to a question.

    Attributes:
        question (ForeignKey): The question to which this answer belongs.
        text (CharField): The text content of the answer.
    """

    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def clean(self):
        """
        Validates the answer instance.

        Raises:
            ValidationError: If the answer text is empty or if the corresponding answer option does not exist for the question.
        """

        if not self.text:
            raise ValidationError("Answer text cannot be empty.")

        Question = apps.get_model('questions', 'Question')
        if not AnswerOption.objects.filter(question=self.question, text=self.text).exists():
            raise ValidationError("Answer option does not exist for this question.")

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure validation before saving.
        """

        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the answer text.
        """

        return self.text
