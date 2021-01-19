"""TouristHelperApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
                  path('api/', views.home, name="home"),
                  path('SubmitCityForm/', views.SubmitCityForm, name="SubmitCityForm"),
                  path('city_details/', views.cityList.as_view()),
                  path('user_profile/<str:email>', csrf_exempt(views.userProfile.as_view())),
                  path('explore_city/<str:city_name>', views.ExploreCityClass.as_view()),
                  path('most_liked_cities/', views.MostLikedCities.as_view()),
                  path('most_visited_cities/', views.MostVisitedCities.as_view()),
                  path('cities_image/<str:city_name>', views.City_Image.as_view())

              ]
