# Generated by Django 3.0.2 on 2020-01-13 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200113_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proximoslancamento',
            name='launch_window',
        ),
        migrations.RemoveField(
            model_name='proximoslancamento',
            name='mission_id',
        ),
    ]
