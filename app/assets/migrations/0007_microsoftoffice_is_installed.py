# Generated by Django 5.0.2 on 2024-02-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_rename_computer_name_microsoftoffice_computer'),
    ]

    operations = [
        migrations.AddField(
            model_name='microsoftoffice',
            name='is_installed',
            field=models.BooleanField(default=False),
        ),
    ]
