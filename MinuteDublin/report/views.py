from django.shortcuts import render

# Create your views here.

import json
import dynamodb.dynamodb_access as ddba
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def report(request):
    last_id = 0
    reports = ddba.get_all_reports()

    for report in reports:
        if int(report["id"]) > last_id:
            last_id = int(report["id"])

    body = json.loads(request.body)

    print(last_id+1, body)

    return JsonResponse(body)


def fetch_reports(request):
    reports = ddba.get_all_reports()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for report in reports:
        item = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [ float(report["longitude"]), float(report["latitude"])]
          },
          "properties": {
            "id": report["id"],
            "type": report["type"],
            "report_time": report["report_time"],
            "comment": report["comment"]
          }
        }
        geo_json["features"].append(item)


    return JsonResponse(geo_json, safe=False, json_dumps_params={"indent": 2})
