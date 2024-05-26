from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from ilm.models import Course, Module, Content
from models import Notification


class NotificationHandler:
    @staticmethod
    @receiver(post_save, sender=Course)
    def notify_course_update(sender, instance, created, **kwargs):
        if created:
            title = "New Course Added"
            message = f"A new course titled '{instance.title}' has been added."
        else:
            title = "Course Updated"
            message = f"The course '{instance.title}' has been updated."

        # Notify all users (customize to target specific users if needed)
        users = User.objects.all()
        for user in users:
            Notification.objects.create(user=user, title=title, message=message)

    @staticmethod
    @receiver(post_save, sender=Module)
    def notify_module_update(sender, instance, created, **kwargs):
        if created:
            title = "New Module Added"
            message = f"A new module titled '{instance.title}' has been added to the course '{instance.course.title}'."
        else:
            title = "Module Updated"
            message = f"The module '{instance.title}' in the course '{instance.course.title}' has been updated."

        # Notify all users (customize to target specific users if needed)
        users = User.objects.all()
        for user in users:
            Notification.objects.create(user=user, title=title, message=message)

    @staticmethod
    @receiver(post_save, sender=Content)
    def notify_content_update(sender, instance, created, **kwargs):
        if created:
            title = "New Content Added"
            message = f"A new content titled '{instance.title}' has been added to the module '{instance.module.title}'."
        else:
            title = "Content Updated"
            message = f"The content '{instance.title}' in the module '{instance.module.title}' has been updated."

        # Notify all users (customize to target specific users if needed)
        users = User.objects.all()
        for user in users:
            Notification.objects.create(user=user, title=title, message=message)
