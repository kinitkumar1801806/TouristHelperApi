from django.contrib import admin
from .models import City, TouristImages, UserProfile, ExploreCity

# Register your models here.
admin.site.register(City)
admin.site.register(TouristImages)
admin.site.register(UserProfile)
admin.site.register(ExploreCity)
