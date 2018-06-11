#!/usr/bin/env python
# (c)2014 John Strickler
from suds.client import Client

NWS_URL = 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl' # <1>

client = Client(NWS_URL) # <2>

for method in client.wsdl.services[0].ports[0].methods: # <3>
    print(method)
