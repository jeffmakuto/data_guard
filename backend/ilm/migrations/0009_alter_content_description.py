# Generated by Django 5.0.6 on 2024-05-17 13:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilm', '0008_alter_module_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)]),
        ),
    ]
