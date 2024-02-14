# Generated by Django 5.0.2 on 2024-02-14 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_alter_computer_monitor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'ordering': ['computer_name']},
        ),
        migrations.AlterModelOptions(
            name='computermodel',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='computertype',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='maker',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='monitor',
            options={'ordering': ['model__name']},
        ),
        migrations.AlterModelOptions(
            name='monitormodel',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='operatingsystem',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='printer',
            options={'ordering': ['ip_addr']},
        ),
        migrations.AlterModelOptions(
            name='printermodel',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['name'], 'verbose_name_plural': 'Statuses'},
        ),
    ]
