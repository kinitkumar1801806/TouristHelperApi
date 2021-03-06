# Generated by Django 3.1.1 on 2020-10-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city_district',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='city',
            name='city_state',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='city',
            name='city_zip',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='city',
            name='airport_details',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='city',
            name='bus_stand_details',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_details',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='railway_station_details',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
