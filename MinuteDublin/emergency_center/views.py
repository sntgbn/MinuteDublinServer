from django.shortcuts import render

# Create your views here.
import fire_stations.firestations_url2lib as fire
import garda_stations.garda_url2lib as garda
import hospitals.hospitals_url2lib as hospital
from django.http import HttpResponse


def create_all(request):
    fire.parse_file()
    garda.parse_file()
    hospital.parse_file()
    return HttpResponse(status=200)


def fetch_fire_brigade():
    return
