#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 21:24:35 2013

"""
from datetime import date as Date

ww2_start = Date(1941, 12, 7)
ww2_end = Date(1945, 8, 15)

elapsed_time = ww2_end - ww2_start

print("World War II lasted {0} days".format(elapsed_time.days))