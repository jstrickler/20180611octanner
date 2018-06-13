#!/usr/bin/env python
# (c) John Strickler 2018
import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')

for president in doc.findall('.//president'):
    name_field = president.find('name')
    first_name = name_field.findtext('first')
    last_name = name_field.findtext('last')
    state = president.findtext('birthstate')
    print(first_name, last_name, state)
