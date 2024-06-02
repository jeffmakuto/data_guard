from django.test import TransactionTestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status


class NotificationAPITest(TransactionTestCase):
    """TestCase for the Notification API endpoint"""
    def setUp(self):
        """setup data for the test case"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_empty_database(self):
        """Test if the database is empty"""
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_single_notification(self):
        """Test if a single notification can be created"""
        # Create a notification
        notification_data = {
            'title': 'Test Title',
            'message': 'Test Message',
            'user': self.user.id
        }
        response = self.client.post('/api/notifications/', {'title': 'Test Title', 'message': 'Test Message', 'user': self.user.id}, format='json')
        print("POST response:", response.status_code, response.data)
        self.assertEqual(response.status_code, 201)
        
        self.assertIn('id', response.data)

        notification_id = response.data['id']
        self.assertEqual(response.data['title'], 'Test Title')
        self.assertEqual(response.data['message'], 'Test Message')

        # Retrieve all notifications
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Title')

        # Update the notification
        updated_notification_data = {'title': 'Updated Title', 'message': 'Updated Message'}
        response = self.client.put(f'/api/notifications/{notification_id}/', updated_notification_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Title')
        self.assertEqual(response.data['message'], 'Updated Message')

        # Delete the notification
        response = self.client.delete(f'/api/notifications/{notification_id}/')
        self.assertEqual(response.status_code, 204)

        # Verify deletion
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)


    def test_multiple_notification(self):
        """Test case for creating multiple notifications"""
        notification1_data = {'title': 'Test Title 1', 'message': 'Test Message 1'}
        notification2_data = {'title': 'Test Title 2', 'message': 'Test Message 2'}
        self.client.post('/api/notifications/', notification1_data, format='json')
        self.client.post('/api/notifications/', notification2_data, format='json')

        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_notification_permissions(self):
        """Test if the notification API endpoint has the correct permissions"""
        self.client.logout()
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)

        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)

    def test_validation(self):
        """Test for validation of Notification data"""
        invalid_data = {'description': 'Test Description'}
        response = self.client.post('/api/notifications/', invalid_data, format='json')
        self.assertEqual(response.status_code, 404)

    def test_error_handling(self):
        """Test for handling errors such as non-existent notifications"""
        response = self.client.get('/api/notifications/630/') #non-existent notification
        self.assertEqual(response.status_code, 404)

        response = self.client.put('/api/notifications/630/', {'title': 'Non-existent Notification', 'message': 'Does not exist'}, format='json')
        self.assertEqual(response.status_code, 404)

        response = self.client.delete('/api/notifications/630/')
        self.assertEqual(response.status_code, 404)