import urllib.request as request
import json
import objects as oo
import serialization as se
from geojson import Feature, FeatureCollection, Point
from geopy.geocoders import Nominatim
import numpy as np
import redis as redis


def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l-1:
        i += 1
        #printi,poly[i], j,poly[j]
        if ((poly[i]["lat"] <= pt["lat"] and pt["lat"] < poly[j]["lat"]) or (poly[j]["lat"] <= pt["lat"] and pt["lat"] < poly[i]["lat"])):
            if (pt["lng"] < (poly[j]["lng"] - poly[i]["lng"]) * (pt["lat"] - poly[i]["lat"]) / (poly[j]["lat"] - poly[i]["lat"]) + poly[i]["lng"]):
                c = not c
        j = i
    return c

dublin_coordinates = [{'lat':53.2099936251, 'lng':-6.2568709764},{'lat':53.2383995869, 'lng':-6.404197593},
                      {'lat':53.2966406056, 'lng':-6.4678633444},{'lat':53.3756575371, 'lng':-6.4741118017},
                      {'lat':53.4151111465, 'lng':-6.4016981933},{'lat':53.4240400411, 'lng':-6.2456373822},
                      {'lat':53.3987380065, 'lng':-6.02341142},  {'lat':53.2510960153, 'lng':-6.0471419289},
                      {'lat':53.2234549302, 'lng':-6.1220412746},{'lat':53.2099936251, 'lng':-6.2568709764}]

with request.urlopen('https://data.smartdublin.ie/cgi-bin/rtpi/busstopinformation?format=json') as response:
    
    # Redis host connection
    redis_host = "minutedublin-001.ivfkmx.0001.use1.cache.amazonaws.com"
    redis_port = 6379
    r = redis.StrictRedis(host=redis_host, port=redis_port)
    
    # Geolocator
    geolocator = Nominatim()

    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        
        print(type(data))
        print(data.keys())
        
        sd_objects = []
        for i in range(len(data['results'])):
            if(isInsidePolygon({'lat':float(data['results'][i]['latitude']), 'lng':float(data['results'][i]['longitude'])}, dublin_coordinates)== True ):
            # if np.sqrt((53.343792 - float(data['results'][i]['latitude']))**2 + (-6.254572 - float(data['results'][i]['longitude']))**2) < 0.08:
                sd_objects.append(oo.Stop(data['results'][i]['stopid'],
                                    data['results'][i]['shortname'],   
                                    oo.Location(float(data['results'][i]['latitude']), float(data['results'][i]['longitude'])),
                                    True))

        feature_collection = []

        for i in range(len(sd_objects)):
            point = Point((sd_objects[i].location.lng, sd_objects[i].location.lat))
            feature = Feature(geometry=point, id=sd_objects[i].ID, properties=dict(name=sd_objects[i].name,
                              isOpen=sd_objects[i].isOpen))
            feature_collection.append(feature)

        geojson_file = FeatureCollection(feature_collection)
        
        with open('bus_stops.geojson', 'w') as outfile:
            json.dump(geojson_file, outfile)
        outfile.close() 
        with open('bus_stops.geojson') as f:
            bus_stops_data = json.load(f)
            r.set('bus_stops', json.dumps(bus_stops_data))
    else:
        print('An error occurred while attempting to retrieve data from the API.')