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

    def test_notification_save(self):
        notification1 = Notification.objects.create(user=self.test_user, title='Test Title 1', message='Test Message 1', read=True)
        notification2 = Notification.objects.create(user=self.test_user, title='Test Title 2', message='Test Message 2', read=False)
        notification1.save()
        notification2.save()
        self.assertTrue(notification1.read)
        self.assertFalse(notification2.read)
        self.assertEqual(list(Notification.objects.all()), [self.notification, notification1, notification2])
        #notification = Notification.objects.all()
        #notification = Notification.objects.save()
        #self.assertTrue(notification.read)
        #self.assertIsNotNone(notification.updated_at)
        #self.assertEqual(notification.updated_at, notification.created_at)
        #self.assertTrue(notification.objects.save())

    def test_notification_category(self):
        notification1 = Notification.objects.create(user=self.test_user, title='Test Title 1', message='Test Message 1', read=False)
        notification2 = Notification.objects.create(user=self.test_user, title='Test Title 2', message='Test Message 2', read=False)
        notification1.category = 'Test Category'
        notification1.save()
        notification2.category = 'Test Category'
        notification2.save()
        self.assertEqual(notification1.category, 'Test Category')
        self.assertEqual(notification2.category, 'Test Category')

    def test_notification_according_to_priority(self):
        notification1 = Notification.objects.create(user=self.test_user, title='Test Title 1', message='Test Message 1', read=False)
        notification2 = Notification.objects.create(user=self.test_user, title='Test Title 2', message='Test Message 2', read=False)
        notification1.priority = 1
        notification1.save()
        notification2.priority = 2
        notification2.save()
        self.assertEqual(notification1.priority, 1)
        self.assertEqual(notification2.priority, 2)
