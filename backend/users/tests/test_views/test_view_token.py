from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class CustomTokenObtainPairViewTests(APITestCase):
    """
    Test cases for CustomTokenObtainPairView.
    """
    def setUp(self):
        """
        Set up a test user and URL for token generation.
        """
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.token_url = reverse('login')

    def test_obtain_token(self):
        """
        Test token generation with valid credentials.
        """
        data = {'username': 'test_user', 'password': 'password123'}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        self.assertTrue('user' in response.data)
        self.assertEqual(response.data['user']['username'], 'test_user')
        # Add more assertions for user data if needed

    def test_invalid_credentials(self):
        """
        Test token generation with invalid credentials.
        """
        data = {'username': 'test_user', 'password': 'wrong_password'}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_missing_credentials(self):
        """
        Test token generation with missing credentials.
        """
        data = {}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_refresh_token(self):
        """
        Test token refresh using a refresh token.
        """
        # Obtain refresh token
        response = self.client.post(self.token_url, {'username': 'test_user', 'password': 'password123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        refresh_token = response.data['refresh']

        # Refresh access token using refresh token
        refresh_url = reverse('token_refresh')
        response = self.client.post(refresh_url, {'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertNotEqual(response.data['access'], '')
