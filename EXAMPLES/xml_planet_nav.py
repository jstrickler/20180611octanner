#!/usr/bin/env python

# import xml.etree.ElementTree as ET # <1>
import lxml.etree as ET

doc = ET.parse('../DATA/solar.xml')  # <2>

root = doc.getroot()  # <3>

for tag in 'inner', 'outer', 'dwarf':  # <4>

    print('{}:'.format(tag.title()))  # <5>
    section = root.find('{}planets'.format(tag))  # <6>
    for planet in section:  # <7>
        print('\t' + planet.get("planetname"))  # <8>
    print()
