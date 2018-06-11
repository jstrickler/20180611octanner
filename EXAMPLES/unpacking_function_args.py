#!/usr/bin/env python
# (c) 2018 CJ Associates
#

people = [ # <1>
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Rattburger', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]

def person_record(first_name, last_name, city, state): # <2>
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))

for person in people:  # <3>
    person_record(*person)  # <4>
