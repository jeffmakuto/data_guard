from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from ilm.models import Module, Course


class ContentAPITest(TransactionTestCase):
    """
    Test case for the Content API endpoints.
    """
    def setUp(self):
        """
        Set up initial data for the test case.
        """
        self.admin_user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.non_admin_user = User.objects.create_user(username='user', password='userpass')
        self.client = APIClient()
        self.course = Course.objects.create(title='Test Course', description='Test Course Description')
        self.module = Module.objects.create(title='Test Module', description='Test Module Description', course=self.course)
        self.client.login(username='admin', password='adminpass')

    def create_mock_file(self, filename, content=b"", content_type="text/plain"):
        """
        Creates a mock file object for testing file uploads.
        """
        return SimpleUploadedFile(filename, content, content_type)

    def test_empty_database(self):
        """
        Test case for verifying the behavior when the database is empty.
        """
        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_content(self):
        """
        Test case for CRUD operations on a single content with file upload validation.
        """
        valid_content_data = {
            'module': self.module.id,
            'title': 'Test Content',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content=b'test content', content_type='audio/mpeg')  # Valid audio file
        }

        response = self.client.post('/api/contents/', valid_content_data, format='multipart')
        self.assertEqual(response.status_code, 201)  # Assuming creation is successful with valid audio
        content_id = response.data['id']

        response = self.client.get(f'/api/contents/{content_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['module'], self.module.id)
        self.assertEqual(response.data['title'], 'Test Content')
        self.assertEqual(response.data['content_type'], 'audio')

        updated_content_data = {
            'module': self.module.id,
            'title': 'Updated Content',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content=b'updated content', content_type='audio/mpeg')  # Valid audio file
        }
        response = self.client.put(f'/api/contents/{content_id}/', updated_content_data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['module'], self.module.id)
        self.assertEqual(response.data['title'], 'Updated Content')
        self.assertEqual(response.data['content_type'], 'audio')

        response = self.client.delete(f'/api/contents/{content_id}/')
        self.assertEqual(response.status_code, 204)

    def test_multiple_contents(self):
        """
        Test case for creating and listing multiple contents with file upload validation.
        """
        content1_data = {
            'module': self.module.id,
            'title': 'Content 1',
            'content_type': 'picture',
            'file': self.create_mock_file('test_image.jpg', content=b'test image content', content_type='image/jpeg')  # Valid image file
        }

        content2_data = {
            'module': self.module.id,
            'title': 'Content 2',
            'content_type': 'video',
            'file': self.create_mock_file('test_video.mp4', content=b'test video content', content_type='video/mp4')  # Valid video file
        }

        response1 = self.client.post('/api/contents/', content1_data, format='multipart')
        self.assertEqual(response1.status_code, 201)

        response2 = self.client.post('/api/contents/', content2_data, format='multipart')
        self.assertEqual(response2.status_code, 201)

        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        content_ids = {content['id'] for content in response.data}
        self.assertIn(response1.data['id'], content_ids)
        self.assertIn(response2.data['id'], content_ids)

    def test_permission(self):
        """
        Test case for verifying permissions for accessing content endpoints.
        """
        self.client.logout()  # Log out admin
        response = self.client.post('/api/contents/', {
            'module': self.module.id,
            'title': 'Test Content',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content_type='audio/mpeg')
        }, format='multipart')
        self.assertEqual(response.status_code, 403)  # Forbidden for non-admins

        self.client.login(username='user', password='userpass')
        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, 200)  # Non-admins can list contents

        response = self.client.post('/api/contents/', {
            'module': self.module.id,
            'title': 'New Content',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content_type='audio/mpeg')
        }, format='multipart')
        self.assertEqual(response.status_code, 403)

        content_data = {
            'module': self.module.id,
            'title': 'Content 1',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content_type='audio/mpeg')
        }
        response = self.client.post('/api/contents/', content_data, format='multipart')
        content_id = response.data.get('id')

        if content_id:
            response = self.client.put(f'/api/contents/{content_id}/', {'title': 'Updated Content'}, format='json')
            self.assertEqual(response.status_code, 403)
            response = self.client.delete(f'/api/contents/{content_id}/')
            self.assertEqual(response.status_code, 403)

    def test_validation(self):
        """
        Test case for validation of content data.
        """
        invalid_data = {
            'module': self.module.id,
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content_type='audio/mpeg')
        }  # Missing 'title' field
        response = self.client.post('/api/contents/', invalid_data, format='multipart')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

        invalid_data = {
            'module': self.module.id,
            'title': '',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content_type='audio/mpeg')
        }  # Empty 'title' field
        response = self.client.post('/api/contents/', invalid_data, format='multipart')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

    def test_error_handling(self):
        """
        Test case for handling errors such as non-existent content ID.
        """
        response = self.client.get('/api/contents/999/')  # Non-existent content ID
        self.assertEqual(response.status_code, 404)  # Not Found

        response = self.client.put('/api/contents/999/', {
            'module': self.module.id,
            'title': 'Non-existent Content',
            'content_type': 'audio',
            'file': self.create_mock_file('test_audio.mp3', content_type='audio/mpeg')
        }, format='multipart')
        self.assertEqual(response.status_code, 404)  # Not Found

        response = self.client.delete('/api/contents/999/')
        self.assertEqual(response.status_code, 404)  # Not Found
