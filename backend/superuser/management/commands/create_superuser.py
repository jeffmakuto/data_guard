from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    """
    A Django management command to create a superuser if it does not already exist.
    
    This command reads the superuser credentials from the environment variables 
    SUPERUSER_USERNAME, SUPERUSER_EMAIL, and SUPERUSER_PASSWORD.
    """

    help = 'Create a superuser if none exists'

    def handle(self, *args, **options):
        """
        The main method that is called when the command is run.
        
        It retrieves the superuser credentials from the environment variables and 
        creates a superuser if one with the specified username does not already exist.
        """
        username = os.getenv('SUPERUSER_USERNAME')
        email = os.getenv('SUPERUSER_EMAIL')
        password = os.getenv('SUPERUSER_PASSWORD')

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
            else:
                self.stdout.write(self.style.WARNING('Superuser already exists.'))
        else:
            self.stdout.write(
                self.style.ERROR(
                    'Missing one or more required environment variables: SUPERUSER_USERNAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD.'
                )
            )
