import xml.etree.ElementTree as ET
import urllib.request
# This should work but doesn't for some reason
import dynamodb.dynamodb_access as ddba
import os



def parse_file():
    # https://data.smartdublin.ie/dataset/4f02d0c7-7091-4339-ba3a-20232d33e357/resource/eb12cb99-695d-4983-bc20-a5856463bb36/download/fccfirestationsp20111201-2134.xml
    xml_file = 'firestations.xml'
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, xml_file)

    firestations_tree = ET.parse(filename)
    firestations = firestations_tree.getroot()[0]

    for firestation in firestations:
        print("_____________________________________________")
        print("Name: " + firestation[0].text) # Name
        print("LAT: " + firestation[-2].text) # LAT
        print("LONG: " + firestation[-1].text) # LONG
        ddba.create_firestation(firestation[0].text, firestation[-2].text, firestation[-1].text)