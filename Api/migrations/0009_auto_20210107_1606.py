# Generated by Django 3.1.4 on 2021-01-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_auto_20210107_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_image',
            field=models.ImageField(default='', upload_to='City/'),
        ),
        migrations.AlterField(
            model_name='touristimages',
            name='image',
            field=models.ImageField(default='', upload_to='tourist_places/'),
        ),
    ]