# Generated by Django 3.1.1 on 2020-10-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20201020_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(default='', upload_to='tourist_places/images'),
        ),
        migrations.AddField(
            model_name='city',
            name='tourist_places',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
