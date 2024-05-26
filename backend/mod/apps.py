from django.apps import AppConfig


class ModConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mod'

    def ready(self):
        """
        Instantiate the signal handlers
        """
        from .models import NotificationHandler
        NotificationHandler()
