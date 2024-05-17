from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Module, Content
from django.core.exceptions import ValidationError


class ContentTestCase(TestCase):
    """
    Class to test the content of the app
    """
    def setUp(self):
        """
        Setup method to create a test Module instance.
        """
        self.module = Module.objects.create(title="Test Module")
    
    def test_content_creation(self):
        """
        Test valid content creation.
        """
        content = Content.objects.create(
            module=self.module,
            title="Test Content",
            content_type="audio",
            file=SimpleUploadedFile("test.mp3", b"")
        )
        self.assertEqual(Content.objects.count(), 1)

    def test_blank_title(self):
        """
        Test creation with blank title.
        """
        with self.assertRaises(ValidationError) as context:
            content = Content(
                module=self.module,
                title="",
                content_type="video",
                file=SimpleUploadedFile("test.mp4", b"")
            )
            content.full_clean()
        self.assertIn('The title field cannot be blank.', context.exception.messages)

    def test_invalid_content_type(self):
        """
        Test creation with invalid content type.
        """
        with self.assertRaises(ValidationError) as context:
            content = Content(
                module=self.module,
                title="Invalid Content",
                content_type="invalid_type",
                file=SimpleUploadedFile("test.txt", b"")
            )
            content.full_clean()
        self.assertIn('Invalid content type', context.exception.messages)

    def test_invalid_file_extension(self):
        """
        Test creation with invalid file extension.
        """
        with self.assertRaises(ValidationError) as context:
            content = Content(
                module=self.module,
                title="Invalid File",
                content_type="picture",
                file=SimpleUploadedFile("test.txt", b"")
            )
            content.full_clean()
        self.assertIn('File extension not allowed', context.exception.messages)

    def test_maximum_title_length(self):
        """
        Test creation with maximum title length.
        """
        long_title = "a" * 101
        with self.assertRaises(ValidationError) as context:
            content = Content(
                module=self.module,
                title=long_title,
                content_type="video",
                file=SimpleUploadedFile("test.mp4", b"")
            )
            content.full_clean()
        self.assertIn('Ensure this value has at most 100 characters', context.exception.messages)

    def test_null_file(self):
        """
        Test creation with null file.
        """
        with self.assertRaises(ValidationError) as context:
            content = Content(
                module=self.module,
                title="Null File",
                content_type="video",
                file=None
            )
            content.full_clean()
        self.assertIn('This field cannot be null.', context.exception.messages)

    def test_invalid_file_size(self):
        """
        Test creation with invalid file size.
        """
        large_file = SimpleUploadedFile("large.mp4", b"0" * (10 * 1024 * 1024 + 1))  # 10MB + 1 byte
        with self.assertRaises(ValidationError) as context:
            content = Content(
                module=self.module,
                title="Large File",
                content_type="video",
                file=large_file
            )
            content.full_clean()
        self.assertIn('File size cannot exceed', context.exception.messages[0])

    def test_unique_title_per_module(self):
        """
        Test unique title per module.
        """
        content1 = Content.objects.create(
            module=self.module,
            title="Unique Title",
            content_type="audio",
            file=SimpleUploadedFile("unique1.mp3", b"")
        )
        with self.assertRaises(ValidationError) as context:
            content2 = Content(
                module=self.module,
                title="Unique Title",
                content_type="video",
                file=SimpleUploadedFile("unique2.mp4", b"")
            )
            content2.full_clean()
        self.assertIn('Content with this Title already exists for this Module.', context.exception.messages)

    def test_multiple_content_creation(self):
        """
        Test creation of multiple contents for a module.
        """
        content1 = Content.objects.create(
            module=self.module,
            title="Content 1",
            content_type="audio",
            file=SimpleUploadedFile("content1.mp3", b"")
        )
        content2 = Content.objects.create(
            module=self.module,
            title="Content 2",
            content_type="video",
            file=SimpleUploadedFile("content2.mp4", b"")
        )
        self.assertEqual(Content.objects.count(), 2)
            
