#!/usr/bin/env python
from datetime import datetime
import time

adate = datetime(1975, 4, 2, 12, 9, 55) # <1>
timestamp = time.mktime(adate.timetuple()) # <2>
today = time.time() # <3>


for ts in 86400, timestamp, today: # <4>
    tm = time.localtime(ts)  # <5>
    print(tm.tm_year, tm.tm_mon, tm.tm_mday)
    print()

    dt = datetime.fromtimestamp(ts)  # <6>
    print(dt.year, dt.month, dt.day)
    print('-' * 20)
