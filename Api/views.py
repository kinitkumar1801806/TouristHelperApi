import json
from django.shortcuts import render
from Api.models import City, TouristImages, UserProfile, ExploreCity
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CitySerializer, UserProfileSerializer, ExploreCitySerializer, CityImage
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


def home(request):
    return render(request, "api/CityEntryForm.html")


def SubmitCityForm(request):
    if request.method == "POST":
        city_count = request.POST.get('city_count', '')
        airport_count = request.POST.get('airport_count', '')
        railway_count = request.POST.get('railway_count', '')
        bus_count = request.POST.get('bus_count', '')
        place_count = request.POST.get('place_count', '')
        ct_dict = {}
        for i in range(int(city_count) + 1):
            city = request.POST.get('rCity' + str(i), '')
            district = request.POST.get('rDistrict' + str(i), '')
            state = request.POST.get('rState' + str(i), '')
            price = request.POST.get('Price' + str(i), '')
            res = json.dumps({'city': city, 'district': district, 'state': state, 'price': price})
            ct_dict['city_no' + str(i)] = res
        city_res = json.dumps(ct_dict)
        airport_dict = {}
        for i in range(int(airport_count) + 1):
            name = request.POST.get('airportName' + str(i), '')
            distance = request.POST.get('airportDistance' + str(i), '')
            price = request.POST.get('airportPrice' + str(i), '')
            res = json.dumps({'name': name, 'distance': distance, 'price': price})
            airport_dict['airport_no' + str(i)] = res
        airport_res = json.dumps(airport_dict)
        railway_dict = {}
        for i in range(int(railway_count) + 1):
            name = request.POST.get('railwayName' + str(i), '')
            distance = request.POST.get('railwayDistance' + str(i), '')
            price = request.POST.get('railwayPrice' + str(i), '')
            res = json.dumps({'name': name, 'distance': distance, 'price': price})
            railway_dict['railway_no' + str(i)] = res
        railway_res = json.dumps(railway_dict)
        bus_dict = {}
        for i in range(int(bus_count) + 1):
            name = request.POST.get('busName' + str(i), '')
            distance = request.POST.get('busDistance' + str(i), '')
            price = request.POST.get('busPrice' + str(i), '')
            res = json.dumps({'name': name, 'distance': distance, 'price': price})
            bus_dict['bus_no' + str(i)] = res
        bus_res = json.dumps(bus_dict)
        place_dict = {}
        image_list = []
        for i in range(int(place_count) + 1):
            name = request.POST.get('placeName' + str(i), '')
            distance = request.POST.get('placeDistance' + str(i), '')
            price = request.POST.get('placePrice' + str(i), '')
            image = request.FILES['placeImage' + str(i)]
            image_list.append(image)
            res = json.dumps({'name': name, 'distance': distance, 'price': price, 'image': image.name})
            place_dict['place_no' + str(i)] = res
        place_res = json.dumps(place_dict)
        city_name = request.POST.get('city', '')
        city_dist = request.POST.get('district', '')
        city_state = request.POST.get('state', '')
        city_zip = request.POST.get('zip', '')
        city_image = request.FILES['image']
        likes = 0
        visits = 0
        explore_city = ExploreCity(city_name=city_name, likes=likes, visits=visits)
        city = City(city_name=city_name, city_district=city_dist, city_state=city_state, city_zip=city_zip,
                    city_image=city_image,
                    city_details=city_res, airport_details=airport_res, railway_station_details=railway_res,
                    bus_stand_details=bus_res, tourist_places=place_res)
        city.save()
        explore_city.save()
        for i in image_list:
            tourist_places = TouristImages(image=i)
            tourist_places.save()
    return render(request, 'api/CityEntryForm.html')


class cityList(APIView):

    def get(self, request):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)


class userProfile(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, email):
        userProfile1 = UserProfile.objects.filter(email=email)
        serializer = UserProfileSerializer(userProfile1, many=True)
        return Response(serializer.data)

    def put(self, request, email):
        userProfile1 = UserProfile.objects.get(email=email)
        serializer = UserProfileSerializer(userProfile1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, email):
        userProfile = UserProfile.objects.filter(email=email)
        if userProfile:
            return Response("Email Already Exists")
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExploreCityClass(APIView):
    def get(self, request, city_name):
        explore_city = ExploreCity.objects.filter(city_name=city_name)
        serializer = ExploreCitySerializer(explore_city, many=True)
        return Response(serializer.data)

    def put(self, request, city_name):
        explore_city = ExploreCity.objects.get(city_name=city_name)
        serializer = ExploreCitySerializer(explore_city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MostLikedCities(APIView):
    def get(self, request):
        explore_city = ExploreCity.objects.all().order_by('-likes')
        serializer = ExploreCitySerializer(explore_city, many=True)
        return Response(serializer.data)


class MostVisitedCities(APIView):
    def get(self, request):
        explore_city = ExploreCity.objects.all().order_by('-visits')
        serializer = ExploreCitySerializer(explore_city, many=True)
        return Response(serializer.data)


class City_Image(APIView):
    def get(self, request, city_name):
        city = City.objects.filter(city_name=city_name)
        serializer = CityImage(city, many=True)
        return Response(serializer.data)
