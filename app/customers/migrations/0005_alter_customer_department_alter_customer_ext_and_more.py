# Generated by Django 5.0.2 on 2024-02-16 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.department'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ext',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
