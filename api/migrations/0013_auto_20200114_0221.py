# Generated by Django 3.0.2 on 2020-01-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_lancamentospassado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamentospassado',
            name='details',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='flight_number',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='is_tentative',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='launch_date_local',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='launch_date_unix',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='launch_date_utc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='launch_year',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='mission_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='tbd',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lancamentospassado',
            name='tentative_max_precision',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximolancamento',
            name='nome',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='details',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='flight_number',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='is_tentative',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='launch_date_local',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='launch_date_unix',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='launch_date_utc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='launch_year',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='mission_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='tbd',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proximoslancamento',
            name='tentative_max_precision',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='ultimolancamento',
            name='nome',
            field=models.CharField(max_length=500),
        ),
    ]
