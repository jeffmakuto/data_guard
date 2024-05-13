from django.test import TestCase
from ilm.models.content import Content


class ContentModelTestCase(TestCase):
    """
    Test case for the Content model class.
    """
    def setUp(self):
        """
        Sets up the test environment by creating a Content instance.
        """
        self.content = Content.objects.create(
            title='Test Content',
            description='This is a test content',
            type='video',
            file_path='/path/to/video.mp4'
        )

    def test_content_creation(self):
        """
        Verifies that content can be created.
        """
        self.assertEqual(self.content.title, 'Test Content')
        self.assertEqual(self.content.description, 'This is a test content')
        self.assertEqual(self.content.type, 'video')
        self.assertEqual(self.content.file_path, '/path/to/video.mp4')