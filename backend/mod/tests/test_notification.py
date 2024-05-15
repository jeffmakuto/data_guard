#!/user/bin/env python

from django.test import TestCase
from mod.models.notification import Notification
from django.contrib.auth.models import User

class NotificationTestCase(TestCase):
    """Notification class test case"""
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='test_user', email='test@example.com', password='test_password')
        cls.notification = Notification.objects.create(user=cls.test_user, title='Test Title', message='Test Message', read=False)

    def test_notification_creation(self):
        notification = Notification.objects.get(id=1)
        self.assertEqual(notification.user.username, 'test_user')
        self.assertEqual(notification.title, 'Test Title')
        self.assertEqual(notification.message, 'Test Message')
        self.assertFalse(notification.read)
        self.assertIsNotNone(notification.created_at)
    
    def test_notification_title_max_length(self):
        notification = self.notification #first access the notification object
        max_length = self.notification._meta.get_field('title').max_length
        self.assertEqual(max_length, 225)

    def test_notification_created_at_auto_add_now(self):
        notification = self.notification #first access the notification object
        self.assertIsNotNone(notification.created_at)

    def test_notification_order(self):
        notification_1 = Notification.objects.create(user=self.test_user, title='Test Title 1', message='Test Message 1', read=False)
        notification_2 = Notification.objects.create(user=self.test_user, title='Test Title 2', message='Test Message 2', read=False)
        notifications = Notification.objects.all()
        self.assertEqual(list(notifications), [self.notification, notification_1, notification_2])