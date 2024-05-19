from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.translation import gettext_lazy as _


class MaxFileSizeValidator:
    """
    Validator to check if the file size does not exceed a specified limit.
    """
    def __init__(self, max_size: int) -> None:
        """
        Initialize the validator with the maximum allowed file size in bytes.
        
        Args:
            max_size (int): The maximum allowed file size in bytes.
        """
        if max_size < 0:
            raise ValueError("Maximum size cannot be negative.")
        self.max_size = max_size

    def __call__(self, value: UploadedFile) -> None:
        """
        Perform the validation check.
        
        Args:
            value (UploadedFile): The uploaded file object to validate.
        
        Raises:
            ValidationError: If the file size exceeds the maximum allowed size.
        """
        if value.size > self.max_size:
            raise ValidationError(
                _('File size cannot exceed %(max_size)s bytes.'),
                params={'max_size': self.max_size},
            )

    def deconstruct(self):
        """
        Serialize the validator for Django migrations.
        
        Returns:
            Tuple: A tuple containing the path to the class and its arguments.
        """
        return ('MaxFileSizeValidator', [self.max_size], {})

