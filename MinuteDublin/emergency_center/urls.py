from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('create_all', views.create_all, name='create_all'),
    path('fetch_fire_brigade', views.fetch_fire_brigade, name='fetch_fire_brigade'),

]