from django.test import TransactionTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from ilm.models import Course


class ModuleAPITest(TransactionTestCase):
    """
    Test case for the Module API endpoints.
    """
    def setUp(self):
        """
        Set up initial data for the test case.
        """
        self.admin_user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.non_admin_user = User.objects.create_user(username='user', password='userpass')
        self.client = APIClient()
        self.course = Course.objects.create(title='Test Course', description='Test Course Description')
        self.client.login(username='admin', password='adminpass')

    def test_empty_database(self):
        """
        Test case for verifying the behavior when the database is empty.
        """
        response = self.client.get('/api/modules/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_module(self):
        """
        Test case for CRUD operations on a single module.
        """
        module_data = {'title': 'Test Module', 'description': 'Test Description', 'course': self.course.id}
        response = self.client.post('/api/modules/', module_data, format='json')
        self.assertEqual(response.status_code, 201)
        module_id = response.data['id']
        self.assertIn('course', response.data)

        response = self.client.get(f'/api/modules/{module_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Module')
        self.assertEqual(response.data['description'], 'Test Description')
        self.assertEqual(response.data['course'], self.course.id)

        updated_module_data = {'title': 'Updated Module', 'description': 'Updated Description', 'course': self.course.id}
        response = self.client.put(f'/api/modules/{module_id}/', updated_module_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Module')
        self.assertEqual(response.data['description'], 'Updated Description')
        self.assertEqual(response.data['course'], self.course.id)

        response = self.client.delete(f'/api/modules/{module_id}/')
        self.assertEqual(response.status_code, 204)

    def test_multiple_modules(self):
        """
        Test case for creating and listing multiple modules.
        """
        module1_data = {'title': 'Module 1', 'description': 'Description 1', 'course': self.course.id}
        module2_data = {'title': 'Module 2', 'description': 'Description 2', 'course': self.course.id}
        self.client.post('/api/modules/', module1_data, format='json')
        self.client.post('/api/modules/', module2_data, format='json')

        response = self.client.get('/api/modules/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_permission(self):
        """
        Test case for verifying permissions for accessing module endpoints.
        """
        self.client.logout()  # Log out admin
        response = self.client.post('/api/modules/', {'title': 'Test Module', 'description': 'Test Description', 'course': self.course.id}, format='json')
        self.assertEqual(response.status_code, 403)  # Forbidden for non-admins

        self.client.login(username='user', password='userpass')
        response = self.client.get('/api/modules/')
        self.assertEqual(response.status_code, 200)  # Non-admins can list modules

        response = self.client.post('/api/modules/', {'title': 'New Module', 'description': 'New Description', 'course': self.course.id}, format='json')
        self.assertEqual(response.status_code, 403)

        module_data = {'title': 'Module 1', 'description': 'Description 1', 'course': self.course.id}
        response = self.client.post('/api/modules/', module_data, format='json')
        module_id = response.data.get('id')

        if module_id:
            response = self.client.put(f'/api/modules/{module_id}/', {'title': 'Updated Module'}, format='json')
            self.assertEqual(response.status_code, 403)
            response = self.client.delete(f'/api/modules/{module_id}/')
            self.assertEqual(response.status_code, 403)

    def test_validation(self):
        """
        Test case for validation of module data.
        """
        invalid_data = {'description': 'Test Description', 'course': self.course.id}  # Missing 'title' field
        response = self.client.post('/api/modules/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

        invalid_data = {'title': '', 'description': 'Test Description', 'course': self.course.id}  # Empty 'title' field
        response = self.client.post('/api/modules/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

    def test_error_handling(self):
        """
        Test case for handling errors such as non-existent module ID.
        """
        response = self.client.get('/api/modules/999/')  # Non-existent module ID
        self.assertEqual(response.status_code, 404)  # Not Found

        response = self.client.put('/api/modules/999/', {'title': 'Non-existent Module', 'description': 'Does not exist', 'course': self.course.id}, format='json')
        self.assertEqual(response.status_code, 404)  # Not Found

        response = self.client.delete('/api/modules/999/')
        self.assertEqual(response.status_code, 404)  # Not Found
