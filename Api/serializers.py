from rest_framework import serializers
from .models import City, UserProfile, ExploreCity


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_name', 'city_district', 'city_state', 'city_zip', 'city_details',
                  'airport_details', 'railway_station_details', 'bus_stand_details')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ExploreCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploreCity
        fields = '__all__'


class CityImage(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_image', 'city_name')
