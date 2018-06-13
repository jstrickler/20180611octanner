#!/usr/bin/env python
# (c) John Strickler 2018

import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

print(doc, '\n')

root = doc.getroot()

print(root, '\n')

for node in root:
    if node.tag.endswith('planets'):
        for planet in node:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"\t{moon.text}")
