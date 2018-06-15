#!/usr/bin/env python
# (c) John Strickler 2018

import datetime
from dateutil.parser import parse
import dateutil.tz

d1 = datetime.datetime.now(dateutil.tz.tzlocal())
d2 = datetime.datetime.now(dateutil.tz.gettz('Europe/Vienna'))
d3 = datetime.datetime.now(dateutil.tz.gettz('Asia/Kolkata'))

print(d1)
print(d2)
print(d3)

ET = dateutil.tz.gettz('America/New_York')
MT = dateutil.tz.gettz('America/Denver')

d4 = datetime.datetime(2017, 10, 1, 3, 4, 5, tzinfo=ET)
d5 = datetime.datetime(2017, 10, 1, 3, 4, 5, tzinfo=MT)

print(d4)
print(d5)
print(d5 - d4)

ds1 = '2018-03-04 05:32PM -4'
ds2 = '2018-03-04 05:32PM -7'

d1 = parse(ds1,`)
d2 = parse(ds2)
print(d1)
print(d2)
print(d2 - d1)







