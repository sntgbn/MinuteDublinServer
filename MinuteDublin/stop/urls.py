from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('train', views.train, name='train'),

]
