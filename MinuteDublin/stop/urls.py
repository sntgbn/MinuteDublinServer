from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('train', views.train, name='train'),
    path('train_geo_json', views.train_geo_json, name='train_geo_json'),

]
