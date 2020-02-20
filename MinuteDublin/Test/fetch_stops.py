import json
import os
import requests
import sys

# import xmltodict
from django.shortcuts import render
from django.http import HttpResponse
from xml.etree import ElementTree
from django.http import JsonResponse

# dynamodb access
import dynamodb.dynamodb_access as ddba
json_file = open("bus_stops.json")
bus_stop_data = json.load(json_file)


# Should we add routes?
for stop_object in bus_stop_data['results']:
    if (stop_object["fullname"] not in [None, ""]) and ddba.is_inside_polygon(float(stop_object["latitude"]), float(stop_object["longitude"]), ddba.dublin_coordinates) == True:
        ddba.create_bus_stop(stop_id=stop_object["stopid"], name=stop_object["fullname"],
                            latitude=stop_object["latitude"], longitude=stop_object["longitude"])
    else:
        pass


