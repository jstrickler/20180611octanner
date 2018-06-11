#!/usr/bin/env python
# (c)2014 John Strickler
import sys

import lxml.etree as ET
from suds.client import Client # <1>

DEBUG = True
NWS_URL = 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl' # <2>

def main(args):
    client = Client(NWS_URL) # <3>

    for zip_code in args:
        lat, lon = get_lat_lon(zip_code, client)
        print("{0}: {1},{2}\n".format(zip_code, lat, lon))


def get_lat_lon(zip, client):

    response = client.service.LatLonListZipCode(zipCodeList=zip)  # <4>

    if DEBUG:
        print("RESPONSE:", response, end='\n\n')

    xml_doc = ET.fromstring(response) # <5>
    result_element = xml_doc.find('latLonList') # <6>
    lat, lon = result_element.text.split(',') # <7>
    return float(lat), float(lon)

    # or, for the minimalist:
    # return ET.fromstring(response).find('latLonList').text.split(',')

if __name__ == '__main__':
    main(sys.argv[1:])
