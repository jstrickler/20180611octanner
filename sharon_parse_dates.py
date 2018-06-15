#!/usr/bin/env python
# (c) John Strickler 2018
import csv
from datetime import date, datetime
from pprint import pprint

data = []

with open('sharon_dates.txt') as sharon_in:
    rdr = csv.reader(sharon_in)
    for datestring, other in rdr:
        year = datestring[:4]
        month = datestring[4:6]
        day = datestring[6:]
        d = date(int(year), int(month), int(day))
#        d = datetime.strptime(datestring, "%Y%m%d").date()
        data.append((d, other))

for adate, other in sorted(data):
    print(adate, other)
