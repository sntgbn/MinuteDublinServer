from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
import json
# import xmltodict
from django.http import HttpResponse
from xml.etree import ElementTree
from django.http import JsonResponse


def train(request):
    response = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')
    root = ElementTree.fromstring(response.content)

    station_data = []

    for station in root:
        station_object = {}
        for station_info in station:
            content = station_info.text
            tag = station_info.tag.replace("{http://api.irishrail.ie/realtime/}", "")
            tag = tag.replace("Station", "")
            tag = tag.lower()
            if tag == "alias":
                continue
            station_object[tag] = content

        station_object["type"] = "train"
        station_data.append(station_object)

    return JsonResponse(station_data, safe=False, json_dumps_params={'indent': 2})


def train_geo_json(request):

    response = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')
    root = ElementTree.fromstring(response.content)

    station_data = []

    for station in root:
        station_object = {}
        for station_info in station:
            content = station_info.text
            tag = station_info.tag.replace("{http://api.irishrail.ie/realtime/}", "")
            tag = tag.replace("Station", "")
            tag = tag.lower()
            if tag == "alias":
                continue
            station_object[tag] = content

        station_object["type"] = "train"
        station_data.append(station_object)

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for station in station_data:
        stop = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [float(station["longitude"]), float(station["latitude"])]
          },
          "properties": {
            "name": station["desc"]
          }
        }
        geo_json["features"].append(stop)

        # print(station, station_data[station])

    return JsonResponse(geo_json, safe=False, json_dumps_params={'indent': 2})

