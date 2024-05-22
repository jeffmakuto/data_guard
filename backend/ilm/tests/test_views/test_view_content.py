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

    def test_empty_database(self):
        """
        Test case for verifying the behavior when the database is empty.
        """
        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_content(self):
        """
        Test case for CRUD operations on a single content.
        """
        content_data = {'title': 'Test Content', 'description': 'Test Description', 'module': self.module.id}
        response = self.client.post('/api/contents/', content_data, format='json')
        self.assertEqual(response.status_code, 201)
        content_id = response.data['id']
        self.assertIn('module', response.data)

        response = self.client.get(f'/api/contents/{content_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Content')
        self.assertEqual(response.data['description'], 'Test Description')
        self.assertEqual(response.data['module'], self.module.id)

        updated_content_data = {'title': 'Updated Content', 'description': 'Updated Description', 'module': self.module.id}
        response = self.client.put(f'/api/contents/{content_id}/', updated_content_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Content')
        self.assertEqual(response.data['description'], 'Updated Description')
        self.assertEqual(response.data['module'], self.module.id)

        response = self.client.delete(f'/api/contents/{content_id}/')
        self.assertEqual(response.status_code, 204)

    def test_multiple_contents(self):
        """
        Test case for creating and listing multiple contents.
        """
        content1_data = {'title': 'Content 1', 'description': 'Description 1', 'module': self.module.id}
        content2_data = {'title': 'Content 2', 'description': 'Description 2', 'module': self.module.id}
        self.client.post('/api/contents/', content1_data, format='json')
        self.client.post('/api/contents/', content2_data, format='json')

        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_permission(self):
        """
        Test case for verifying permissions for accessing content endpoints.
        """
        self.client.logout()  # Log out admin
        response = self.client.post('/api/contents/', {'title': 'Test Content', 'description': 'Test Description', 'module': self.module.id}, format='json')
        self.assertEqual(response.status_code, 403)  # Forbidden for non-admins

        self.client.login(username='user', password='userpass')
        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, 200)  # Non-admins can list contents

        response = self.client.post('/api/contents/', {'title': 'New Content', 'description': 'New Description', 'module': self.module.id}, format='json')
        self.assertEqual(response.status_code, 403)

        content_data = {'title': 'Content 1', 'description': 'Description 1', 'module': self.module.id}
        response = self.client.post('/api/contents/', content_data, format='json')
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
        invalid_data = {'description': 'Test Description', 'module': self.module.id}  # Missing 'title' field
        response = self.client.post('/api/contents/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

        invalid_data = {'title': '', 'description': 'Test Description', 'module': self.module.id}  # Empty 'title' field
        response = self.client.post('/api/contents/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

    def test_error_handling(self):
        """
        Test case for handling errors such as non-existent content ID.
        """
        response = self.client.get('/api/contents/999/')  # Non-existent content ID
        self.assertEqual(response.status_code, 404)  # Not Found

        response = self.client.put('/api/contents/999/', {'title': 'Non-existent Content', 'description': 'Does not exist', 'module': self.module.id}, format='json')
        self.assertEqual(response.status_code, 404)  # Not Found

        response = self.client.delete('/api/contents/999/')
        self.assertEqual(response.status_code, 404)  # Not Found
