from django.shortcuts import render

# Create your views here.
import fire_stations.firestations_url2lib as fire
import garda_stations.garda_url2lib as garda
import hospitals.hospitals_url2lib as hospital
from django.http import HttpResponse
from django.http import JsonResponse
import dynamodb.dynamodb_access as ddba



def create_all(request):
    fire.parse_file()
    garda.parse_file()
    hospital.parse_file()
    return HttpResponse(status=200)


def fetch_fire_brigade(request):

    stations = ddba.get_all_firestations()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for station in stations:
        item = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [ float(station["longitude"]), float(station["latitude"])]
          },
          "properties": {
            "name": station["name"]
          }
        }
        geo_json["features"].append(item)

    return JsonResponse(geo_json, safe=False, json_dumps_params={"indent": 2})


def fetch_healthcare(request):

    stations = ddba.get_all_hospitals()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for station in stations:
        item = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [ float(station["longitude"]), float(station["latitude"])]
          },
          "properties": {
            "name": station["name"]
          }
        }
        geo_json["features"].append(item)

    return JsonResponse(geo_json, safe=False, json_dumps_params={"indent": 2})

def fetch_garda(request):

    stations = ddba.get_all_gardastations()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for station in stations:
        item = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [ float(station["longitude"]), float(station["latitude"])]
          },
          "properties": {
            "name": station["name"]
          }
        }
        geo_json["features"].append(item)

    return JsonResponse(geo_json, safe=False, json_dumps_params={"indent": 2})