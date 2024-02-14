# Generated by Django 5.0.2 on 2024-02-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_computer_monitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='monitor',
            field=models.ManyToManyField(blank=True, related_name='monitors', to='assets.monitor'),
        ),
    ]