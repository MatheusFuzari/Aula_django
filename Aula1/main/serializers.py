from rest_framework import routers, serializers, viewsets
from .models import *

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
        many = True

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
        many = True

class StarshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starships
        fields = '__all__'
        many = True
