from django.shortcuts import render

import requests
import json
# import xmltodict
from django.http import HttpResponse
from xml.etree import ElementTree
from django.http import JsonResponse
import dynamodb.dynamodb_access as ddba


def train(request):
    trains = ddba.get_all_trains()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for train in trains:
        stop = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [ float(train["longitude"]), float(train["latitude"])]
          },
          "properties": {
            "code": train["code"],
            "id": train["id"],
            "timestamp": train["time_fetched"],
            "direction": train["direction"],
            "type":"train",
          }
        }
        geo_json["features"].append(stop)

    return JsonResponse(geo_json, safe=False, json_dumps_params={'indent': 2})


def transport(request):

    return "hello"
