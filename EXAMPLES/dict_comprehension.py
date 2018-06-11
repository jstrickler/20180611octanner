#!/usr/bin/env python


animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']
# dictionary comprehension
d = {a.lower(): len(a) for a in animals} # <1>
print(d)

