# Generated by Django 5.0.2 on 2024-02-26 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0026_remove_computer_dept_alter_computer_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='site',
        ),
    ]
