# Generated by Django 4.2.7 on 2024-05-25 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0003_delete_bucket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]