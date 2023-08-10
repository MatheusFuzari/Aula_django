from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest

class PeopleAPIView(APIView):
    def get(self, id = ''):
        if(id == ''):
            all_people = People.objects.all()  # Select * from People;
            people_serialized = PeopleSerializer(all_people, many=True) # Python -> JSON
            return Response(people_serialized.data)
        else:
            people = People.objects.get(id=id)
            people_serialized = PeopleSerializer(people, many=True) # Python -> JSON
            return Response(people_serialized.data)
    
class PlanetAPIView(APIView):
    def get(self, request):
        all_planets = Planet.objects.all()
        planet_serialized = PlanetSerializer(all_planets)
        return Response(planet_serialized.data)
        
class StarshipsAPIView(APIView):
    def get(self, request):
        all_starships = Starships.objects.all()
        starships_serialized = StarshipsSerializer(all_starships)
        return Response(starships_serialized.data)