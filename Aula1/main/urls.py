from .views import *
from django.urls import path, include

urlpatterns = [
    path('people/', PeopleAPIView.as_view(), name='people'),
    path('people/<int:id>', PeopleAPIView.as_view(), name='peopleParameter'),
    path('planet/', PlanetAPIView.as_view(), name='planet'),
    path('planet/<int:pk>', PlanetAPIView.as_view(), name='planetParameter'),
    path('starships/', StarshipsAPIView.as_view(), name='starships'),
    path('starships/<int:pk>', StarshipsAPIView.as_view(), name='starshipsParameter')
]
