# Create your views here.
from django.shortcuts import render
import requests
import json
# import xmltodict
from django.http import HttpResponse
from xml.etree import ElementTree
from django.http import JsonResponse
# dynamodb access
import dynamodb.dynamodb_access as ddba


def bus_stops(request):
    json_file = open("bus_stops.json")
    bus_stop_data = json.load(json_file)
    stop_data = []

    # Should we add routes?
    for stop_object in bus_stop_data['results']:
        if (stop_object["fullname"] not in [None, ""]) and ddba.is_inside_polygon(float(stop_object["latitude"]), float(stop_object["longitude"]), ddba.dublin_coordinates) == True:
            ddba.create_bus_stop(stop_id=stop_object["stopid"], name=stop_object["fullname"],
                                latitude=stop_object["latitude"], longitude=stop_object["longitude"])
            stop_data.append(stop_object)
        else:
            pass
    # What should be the response from Json on this?
    return JsonResponse(stop_data, safe=False, json_dumps_params={"indent": 2})


def bus_stops_geo_json(request):
    bus_stop_data = ddba.get_all_bus_stops()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for bus_stop in bus_stop_data:
        stop = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [float(bus_stop["latitude"]), float(bus_stop["longitude"])]
          },
          "properties": {
            "name": bus_stop["name"],
            "id": bus_stop["id"],
            "timestamp": bus_stop["timestamp"],
            "type":"train",
          }
        }
        geo_json["features"].append(stop)
    # Getting JSON response
    return JsonResponse(geo_json, safe=False, json_dumps_params={"indent": 2})


