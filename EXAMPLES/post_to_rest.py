#!/usr/bin/env python
# (c)2015 John Strickler

import requests
import datetime as dt
import time

# NOTE: http://requestb.in has been shut down by the owners due to repeated abuse.

# note: go to http://requestb.in/ and create a new RequestBin -- put the URL here:
#   then go to http://requestb.in/, select the bin, and view the results

URL = 'http://requestb.in/r5ay2pr5'  # <1>

for i in range(5):
    response = requests.post( # <2>
        URL,
        data={'date': dt.datetime.now(),
              'label': 'test_' + str(i)
              }

    )
    time.sleep(.5)

    print(response.status_code)
    print(response.content.decode())

