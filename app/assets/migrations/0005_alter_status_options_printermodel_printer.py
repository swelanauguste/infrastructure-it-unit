# Generated by Django 5.0.2 on 2024-02-13 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_alter_computer_model_alter_computermodel_hdd_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.maker')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('computer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(max_length=100)),
                ('ip_addr', models.GenericIPAddressField(blank=True, null=True)),
                ('dept', models.CharField(blank=True, max_length=100, null=True)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('date_installed', models.DateField(blank=True, null=True)),
                ('warranty_info', models.CharField(max_length=100)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.status')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='assets.printermodel')),
            ],
        ),
    ]
