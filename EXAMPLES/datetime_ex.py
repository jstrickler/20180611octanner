#!/usr/bin/env python

from datetime import datetime, date, timedelta

print("date.today():",date.today()) # <1>

now = datetime.now()  # <2>
print("now.day:", now.day)  # <3>
print("now.month:", now.month)
print("now.year:", now.year)
print("now.hour:", now.hour)
print("now.minute:", now.minute)
print("now.second:", now.second)

d1 = datetime(2007, 6, 13) # <4>
d2 = datetime(2007, 8, 24)

d3 = d2 - d1  # <5>

print("raw time delta:", d3)
print("time delta days:", d3.days)  # <6>

interval = timedelta(10)  # <7>
print("interval:", interval)

d4 = d2 + interval  # <8>
d5 = d2 - interval
print("d2 + interval:", d4)
print("d2 - interval:", d5)
print()

t1 = datetime(2013, 8, 24, 10, 4, 34)  # <9>
t2 = datetime(2015, 8, 24, 22, 8, 1)
t3 = t2 - t1

print("datetime(2007, 8, 24, 10, 4, 34):", t1)
print("datetime(2007, 8, 24, 22, 8, 1):", t2)
print("time diff (t2 - t1):", t3)
