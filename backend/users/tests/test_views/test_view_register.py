from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegisterViewTests(APITestCase):
    def test_register_new_user_success(self):
        """
        Ensure a new user can be registered successfully.
        """
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_register_existing_user_fails(self):
        """
        Ensure registering a user with an existing username fails.
        """
        User.objects.create_user(username='existinguser', password='testpassword')
        url = reverse('register')
        data = {'username': 'existinguser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
