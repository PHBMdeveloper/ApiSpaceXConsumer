# Generated by Django 3.0.2 on 2020-01-13 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200112_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='proximoslancamento',
            name='mission_id',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]