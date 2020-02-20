from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('bus_stop', views.bus_stop, name='bus_stop'),
    path('bus_stop', views.bus_stop_geo_json, name='train_geo_json'),
]
