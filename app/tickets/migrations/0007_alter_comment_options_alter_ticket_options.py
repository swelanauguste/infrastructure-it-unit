# Generated by Django 5.0.2 on 2024-02-20 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-created_at']},
        ),
    ]
