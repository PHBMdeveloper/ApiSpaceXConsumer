# Generated by Django 3.0.2 on 2020-01-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200113_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proximoslancamento',
            name='launch_date_local',
            field=models.CharField(max_length=150),
        ),
    ]
