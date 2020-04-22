import xml.etree.ElementTree as ET
import urllib.request
# http://data.fingal.ie/datasets/xml/Garda_Stations.xml
garda_stations = 'garda.xml'

garda_tree = ET.parse(garda_stations)
stations = garda_tree.getroot()[0]

for station in stations:
    print("_____________________________________________")
    print("Name: " + station[0].text) # Name
    print("Phone: " + station[4].text) # Phone
    print("LAT: " + station[-2].text) # LAT
    print("LONG: " + station[-1].text) # LONG
    ddba.create_gardastation(station[0].text, station[-2].text, station[-1].text)