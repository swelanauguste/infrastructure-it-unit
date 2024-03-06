# Generated by Django 5.0.2 on 2024-03-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_alter_computername_last_used_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computername',
            name='computer_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='computername',
            name='last_used_number',
            field=models.IntegerField(default=0),
        ),
    ]