from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from ilm.models.validators import MaxFileSizeValidator
from django.core.exceptions import ValidationError


class MaxFileSizeValidatorTestCase(TestCase):
    def test_valid_file_size(self):
        """
        Test with a file size that is within the allowed limit.
        """
        validator = MaxFileSizeValidator(max_size=10 * 1024)  # 10 KB limit
        file = SimpleUploadedFile(
            "test.txt", b"0" * (10 * 1024)
        )  # Exactly 10 KB
        # No exception should be raised
        validator(file)

    def test_invalid_file_size(self):
        """
        Test with a file size that exceeds the allowed limit.
        """
        validator = MaxFileSizeValidator(max_size=10 * 1024)  # 10 KB limit
        file = SimpleUploadedFile(
            "test.txt", b"0" * (10 * 1024 + 1)
        )  # 1 byte more than 10 KB
        with self.assertRaises(ValidationError) as context:
            validator(file)
        self.assertEqual(
            context.exception.messages, ['File size cannot exceed 10240 bytes.']
        )

    def test_zero_file_size(self):
        """
        Test with a file size of zero bytes.
        """
        validator = MaxFileSizeValidator(max_size=10 * 1024)  # 10 KB limit
        file = SimpleUploadedFile("test.txt", b"")
        # No exception should be raised
        validator(file)

    def test_negative_max_size(self):
        """
        Test with a negative maximum size limit.
        """
        with self.assertRaises(ValueError):
            MaxFileSizeValidator(max_size=-1)

    def test_large_max_size(self):
        """
        Test with a very large maximum size limit.
        """
        validator = MaxFileSizeValidator(
            max_size=1024 * 1024 * 1024
        )  # 1 GB limit
        file = SimpleUploadedFile(
            "test.txt", b"0" * (1024 * 1024 * 512)
        )  # Exactly 512 MB
        # No exception should be raised
        validator(file)

    def test_zero_max_size(self):
        """
        Test with a maximum size limit of zero bytes.
        """
        validator = MaxFileSizeValidator(max_size=0)
        file = SimpleUploadedFile("test.txt", b"0" * 1024)
        with self.assertRaises(ValidationError) as context:
            validator(file)
        self.assertEqual(
            context.exception.messages, ['File size cannot exceed 0 bytes.']
        )
