# Generated by Django 3.2.25 on 2024-05-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
