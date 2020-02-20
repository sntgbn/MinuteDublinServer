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


def train(request):
    response = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
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
        if ddba.is_inside_polygon(float(station_object["latitude"]), float(station_object["longitude"]), ddba.dublin_coordinates) == True:
            station_object["type"] = "train"
            station_data.append(station_object)
            ddba.create_train_stop(stop_id=station_object["code"], name=station_object["desc"],
                                latitude=station_object["latitude"], longitude=station_object["longitude"])
        else:
            pass
    # What should be the response from Json on this?
    return JsonResponse(station_data, safe=False, json_dumps_params={"indent": 2})


def train_geo_json(request):

    station_data = ddba.get_all_train_stops()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for station in station_data:
        stop = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [float(station["latitude"]), float(station["longitude"])]
          },
          "properties": {
            "name": station["name"],
            "id": station["id"],
            "timestamp": station["timestamp"],
            "type":"train",
          }
        }
        geo_json["features"].append(stop)

        # print(station, station_data[station])
    return JsonResponse(geo_json, safe=False, json_dumps_params={"indent": 2})


