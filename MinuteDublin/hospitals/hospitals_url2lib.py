import xml.etree.ElementTree as ET
import urllib.request
import dynamodb.dynamodb_access as ddba

# https://data.smartdublin.ie/dataset/c5ebc2cf-6047-41cd-aef6-79cc1aef7fe4/resource/a166ddac-2e6e-4582-b546-7a626dcb8778/download/fcchealthcentresp20111201-2134.xml
hospitals = 'hospitals.xml'

hospitals_tree = ET.parse(hospitals)
hospitals = hospitals_tree.getroot()[0]

for hospital in hospitals:
    print("_____________________________________________")
    print("Name: " + hospital[0].text) # Name
    print("LAT: " + hospital[-2].text) # LAT
    print("LONG: " + hospital[-1].text) # LONG