from django.test import TransactionTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class CourseAPITest(TransactionTestCase):
    """
    Test case for the Course API endpoints.
    """
    def setUp(self):
        """
        Set up initial data for the test case.
        """
        self.user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.client = APIClient()
        self.client.login(username='admin', password='adminpass')

    def test_empty_database(self):
        """
        Test case for verifying the behavior when the database is empty.
        """
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_course(self):
        """
        Test case for CRUD operations on a single course.
        """
        course_data = {'title': 'Test Course', 'description': 'Test Description'}
        response = self.client.post('/api/courses/', course_data, format='json')
        self.assertEqual(response.status_code, 201)
        course_id = response.data['id']

        response = self.client.get(f'/api/courses/{course_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Course')

        updated_course_data = {'title': 'Updated Course', 'description': 'Updated Description'}
        response = self.client.put(f'/api/courses/{course_id}/', updated_course_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Course')

        response = self.client.delete(f'/api/courses/{course_id}/')
        self.assertEqual(response.status_code, 204)

    def test_multiple_courses(self):
        """
        Test case for creating and listing multiple courses.
        """
        course1_data = {'title': 'Course 1', 'description': 'Description 1'}
        course2_data = {'title': 'Course 2', 'description': 'Description 2'}
        self.client.post('/api/courses/', course1_data, format='json')
        self.client.post('/api/courses/', course2_data, format='json')

        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_permission(self):
        """
        Test case for verifying permissions for accessing course endpoints.
        """
        self.client.logout()  # Log out admin
        response = self.client.post('/api/courses/', {'title': 'Test Course', 'description': 'Test Description'}, format='json')
        self.assertEqual(response.status_code, 403)  # Forbidden for non-admins

        # Create a non-admin user
        non_admin = User.objects.create_user(username='user', password='userpass')
        self.client.login(username='user', password='userpass')
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)  # Non-admins can list courses

    def test_validation(self):
        """
        Test case for validation of course data.
        """
        invalid_data = {'description': 'Test Description'} # Missing 'title' field
        response = self.client.post('/api/courses/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400)  # Bad Request due to validation error

    def test_error_handling(self):
        """
        Test case for handling errors such as non-existent course ID.
        """
        response = self.client.get('/api/courses/999/')  # Non-existent course ID
        self.assertEqual(response.status_code, 404)  # Not Found
