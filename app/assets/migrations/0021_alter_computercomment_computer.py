# Generated by Django 5.0.2 on 2024-02-23 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0020_computercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computercomment',
            name='computer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='assets.computer'),
        ),
    ]
