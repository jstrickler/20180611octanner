#!/usr/bin/env python
# (c) John Strickler 2018
#!/usr/bin/env python
# (c) John Strickler 2018

import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"\t{moon.text}")
