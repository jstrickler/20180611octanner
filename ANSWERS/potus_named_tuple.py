#!/usr/bin/python

from datetime import date
from collections import namedtuple

field_list = '''
term
last_name
first_name
birth_date
death_date
birthplace
birth_state
took_office
left_office
party
'''.split()

President = namedtuple('President', field_list)

def mkdate(year, month, day):
    if year:
        return date(int(year), int(month), int(day) )
    else:
        return date.today()

presidents = []

with open("../DATA/presidents.txt") as pfile:
    for line in pfile:
        fields = line.rstrip('\n\r').split(":")
        president = President(*fields)
        presidents.append(president)

for pres in presidents:
    print(pres.first_name, pres.last_name, pres.party)
