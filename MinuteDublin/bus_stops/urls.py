from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('bus_stops', views.bus_stops, name='bus_stops'),
    path('bus_stops_geo_json', views.bus_stops_geo_json, name='bus_stops_geo_json'),
]
