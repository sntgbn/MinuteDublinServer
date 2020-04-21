from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('report', views.report, name='report'),
    path('fetch_reports', views.fetch_reports, name='fetch_reports'),

]
