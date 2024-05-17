from django.core.exceptions import ValidationError
from django.test import TestCase
from ilm.models.modules import Module
from ilm.models.content import Content

class ContentModelTestCase(TestCase):
    def setUp(self):
        """
        Creating test data for Content and related Module.
        """
        self.module = Module.objects.create(
            title='Test Module',
            description='This is a test module description.'
        )

        self.content_data = {
            'module': self.module,
            'title': 'Test Content',
            'description': 'This is a test content description',
            'type': 'document',
            'file_path': '/path/to/document.pdf'
        }

    def test_content_creation(self):
        """
        Test if content can be created.
        """
        content = Content.objects.create(**self.content_data)
        self.assertEqual(content.title, self.content_data['title'])
        self.assertEqual(content.description, self.content_data['description'])
        self.assertEqual(content.type, self.content_data['type'])
        self.assertEqual(content.file_path, self.content_data['file_path'])
        self.assertEqual(content.module, self.module)

    def test_content_str_representation(self):
        """
        Test if the string representation of the content is correct.
        """
        content = Content.objects.create(**self.content_data)
        expected_str = f"Title: {self.content_data['title']} : {self.content_data['description']}\nType: Document \nFile Path: {self.content_data['file_path']}"
        self.assertEqual(str(content), expected_str)

    def test_content_description_optional(self):
        """
        Test if content creation succeeds even if description is not provided.
        """
        content_data_without_description = {
            'title': 'Test Content Without Description',
            'type': 'audio',
            'file_path': '/path/to/audio.mp3'
        }
        content = Content.objects.create(**content_data_without_description)
        self.assertEqual(content.title, content_data_without_description['title'])
        self.assertIsNone(content.description)

    def test_content_attributes_type(self):
        """
        Test if content attributes have the correct types.
        """
        content = Content.objects.create(**self.content_data)
        self.assertIsInstance(content.module, Module)
        self.assertIsInstance(content.title, str)
        self.assertIsInstance(content.description, str)
        self.assertIsInstance(content.type, str)
        self.assertIsInstance(content.file_path, str)

    def test_blank_title_constraint(self):
        """
        Test blank constraint on title.
        
        Ensure that creating content without a
        title raises a ValidationError.
        """
        content_data_without_title = {
            'description': 'Test description without title',
            'type': 'video',
            'file_path': '/path/to/video.mp4'
        }
        content = Content(**content_data_without_title)
        with self.assertRaises(ValidationError):
            content.full_clean()

    def test_blank_type_constraint(self):
        """
        Test blank constraint on type.
        
        Ensure that creating content without a
        type raises a ValidationError.
        """
        content_data_without_type = {
            'title': 'Test Content Without Type',
            'description': 'This content has no type',
            'file_path': '/path/to/file'
        }
        content = Content(**content_data_without_type)
        with self.assertRaises(ValidationError):
            content.full_clean()

    def test_blank_file_path_constraint(self):
        """
        Test blank constraint on file_path.
        
        Ensure that creating content without a
        file_path raises a ValidationError.
        """
        content_data_without_file_path = {
            'title': 'Test Content Without File Path',
            'description': 'This content has no file path',
            'type': 'document'
        }
        content = Content(**content_data_without_file_path)
        with self.assertRaises(ValidationError):
            content.full_clean()

    def test_content_description_max_length(self):
        """
        Test maximum length constraint on description.
        """
        long_description = "a" * 1001  # Exceeds the max length of TextField
        content_data_long_description = {
            'title': 'Content with Long Description',
            'description': long_description,
            'type': 'audio',
            'file_path': '/path/to/audio.mp3'
        }
        content = Content(**content_data_long_description)
        with self.assertRaises(ValidationError):
            content.full_clean()

    def test_update_content(self):
        """
        Verify that you can update the attributes of existing content.
        """
        content = Content.objects.create(**self.content_data)
        new_title = 'Updated Title'
        new_description = 'Updated Description'
        new_type = 'video'
        new_file_path = '/new/path/to/video.mp4'
        content.title = new_title
        content.description = new_description
        content.type = new_type
        content.file_path = new_file_path
        content.save()
        # Retrieve the content again from the database
        # to ensure changes are persisted
        updated_content = Content.objects.get(pk=content.pk)
        self.assertEqual(updated_content.title, new_title)
        self.assertEqual(updated_content.description, new_description)
        self.assertEqual(updated_content.type, new_type)
        self.assertEqual(updated_content.file_path, new_file_path)

    def test_delete_content(self):
        """
        Test deleting content.
        """
        content = Content.objects.create(**self.content_data)
        content_id = content.id
        content.delete()
        with self.assertRaises(Content.DoesNotExist):
            Content.objects.get(pk=content_id)
