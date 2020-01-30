from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
# import xmltodict
from django.http import HttpResponse
from xml.etree import ElementTree


def train(request):
    response = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')
    root = ElementTree.fromstring(response.content)

    station_data = []
    # print(root.tag,  "\n", root.attrib)
    # response = xmltodict.parse(response)
    # print(response.status_code,)


    for station in root:
        station_object = {}
        for station_info in station:
            content = station_info.text
            tag = station_info.tag == '{http://api.irishrail.ie/realtime/}StationAlias'

            print(content, tag)
        station_data.append(station_object)

    # geodata = response.json()
    # return render(request, 'core/home.html', {
    #     'ip': geodata['ip'],
    #     'country': geodata['country_name']
    # })
    text = """<h1>welcome to my app !</h1>"""

    return HttpResponse({'response': station_data})
