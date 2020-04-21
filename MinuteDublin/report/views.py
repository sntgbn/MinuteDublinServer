from django.shortcuts import render

# Create your views here.


import dynamodb.dynamodb_access as ddba
from django.http import JsonResponse

def report(request):

    return


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
