# Generated by Django 5.0.2 on 2024-02-14 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_remove_printer_warranty_info_computer_notes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='monitor_models/')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.maker')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('monitor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('dept', models.CharField(blank=True, max_length=100, null=True)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('date_installed', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, help_text='Warranty Information', null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.status')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitors', to='assets.monitormodel')),
            ],
        ),
    ]