# Generated by Django 5.0.2 on 2024-02-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_microsoftofficeversion_microsoftoffice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microsoftoffice',
            name='date_installed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
