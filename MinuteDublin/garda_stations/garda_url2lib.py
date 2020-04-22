import xml.etree.ElementTree as ET
import dynamodb.dynamodb_access as ddba
import urllib.request
import os

def parse_file():
    # http://data.fingal.ie/datasets/xml/Garda_Stations.xml
    xml_file = 'garda.xml'

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, xml_file)

    garda_tree = ET.parse(filename)
    stations = garda_tree.getroot()[0]

    for station in stations:
        print("_____________________________________________")
        print("Name: " + station[0].text) # Name
        print("Phone: " + station[4].text) # Phone
        print("LAT: " + station[-2].text) # LAT
        print("LONG: " + station[-1].text) # LONG
        ddba.create_gardastation(station[0].text, station[-2].text, station[-1].text)