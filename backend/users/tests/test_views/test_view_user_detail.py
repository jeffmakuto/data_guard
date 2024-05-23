from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class UserDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.url = reverse('user_detail')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_retrieve_user_detail(self):
        """
        Ensure user details can be retrieved.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user_detail(self):
        """
        Ensure user details can be updated.
        """
        data = {'first_name': 'Updated', 'last_name': 'User'}
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'User')

    def test_unauthorized_access_fails(self):
        """
        Ensure unauthenticated users cannot access user details.
        """
        self.client.credentials()  # Remove authentication
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
