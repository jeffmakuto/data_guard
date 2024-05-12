from django.apps import AppConfig
from .models import signals
from django.core.exceptions import ValidationError
from typing import Any


class IlmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ilm'

    def ready(self) -> None:
        """
        Connect receivers to the signals.
        """
        answer_saved.connect(validate_answer)
        answer_option_saved.connect(validate_answer_option)

    def validate_answer(sender: Any, instance: Any, **kwargs: Any) -> None:
        """
        Validation logic for Answer model.
        """
        if not instance.question.options.filter(text=instance.text).exists():
            raise ValidationError(f"{instance.text} is not a valid option for the question.")

    def validate_answer_option(sender: Any, instance: Any, **kwargs: Any) -> None:
        """
        Validation logic for AnswerOption model.
        """
        if instance.question.options.filter(text=instance.text).exists():
            raise ValidationError(f"Duplicate answer option: {instance.text}")
