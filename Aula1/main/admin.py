from django.contrib import admin
from .models import * #importando o People e o Planet!!!

# Register your models here.
@admin.register(People)
class detPeople(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ['id','name']

#registra as configurações realizadas do model na página de admin


@admin.register(Planet)
class detPlanet(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin

@admin.register(Starships)
class detStarship(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin