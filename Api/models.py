from django.db import models


class City(models.Model):
    entry_no = models.AutoField
    city_name = models.CharField(max_length=200, default="")
    city_district = models.CharField(max_length=200, default="")
    city_state = models.CharField(max_length=200, default="")
    city_zip = models.CharField(max_length=10, default="")
    city_image = models.ImageField(upload_to='City/', default="")
    city_details = models.CharField(max_length=10000, default="")
    airport_details = models.CharField(max_length=2000, default="")
    railway_station_details = models.CharField(max_length=2000, default="")
    bus_stand_details = models.CharField(max_length=2000, default="")
    tourist_places = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.city_name


class UserProfile(models.Model):
    username = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=30, default="")
    contact = models.CharField(max_length=13, default="")
    description = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=15, default="")
    location = models.CharField(max_length=100, default="")
    liked_cities = models.CharField(max_length=20000, default="")

    def __str__(self):
        return self.username


class TouristImages(models.Model):
    image = models.ImageField(upload_to='tourist_places/', default="")

    def __str__(self):
        return str(self.image)


class ExploreCity(models.Model):
    city_name = models.CharField(max_length=200, default="")
    likes = models.IntegerField(default=0)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return str(self.city_name)
