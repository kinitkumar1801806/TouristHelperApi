# Generated by Django 3.1.4 on 2020-12-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_userprofile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExploreCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='', max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
