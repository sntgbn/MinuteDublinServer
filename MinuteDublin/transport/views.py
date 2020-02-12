from django.shortcuts import render

import requests
import json
# import xmltodict
from django.http import HttpResponse
from xml.etree import ElementTree
from django.http import JsonResponse


def train(request):
    # response = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')
    # root = ElementTree.fromstring(response.content)
    #
    # station_data = []
    #
    # for station in root:
    #     station_object = {}
    #     for station_info in station:
    #         content = station_info.text
    #         tag = station_info.tag.replace("{http://api.irishrail.ie/realtime/}", "")
    #         tag = tag.replace("Station", "")
    #         tag = tag.lower()
    #         if tag == "alias":
    #             continue
    #         station_object[tag] = content
    #
    #     station_object["type"] = "train"
    #     station_data.append(station_object)

    trains = []
    base_train_request = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode="
    # for station in station_data:
    train_object = {}
    response = requests.get(base_train_request+"PERSE")
    root = ElementTree.fromstring(response.content)

    for train in root:
        train_object = {}
        for train_info in train:
            tag = train_info.tag.replace("{http://api.irishrail.ie/realtime/}", "")
            content = train_info.text
            tag = tag.lower()
            train_object[tag] = content
            print(tag, content);

        trains.append(train_object)


    return JsonResponse(trains, safe=False, json_dumps_params={'indent': 2})


def transport(request):

    return "hello"
