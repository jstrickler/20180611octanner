#!/usr/bin/env python

import sys
import os

os.system("hostname")   # <1>

with os.popen('netstat -an') as netstat_in:  # <2>
    for entry in netstat_in:  # <3>
        if 'ESTAB' in entry:   # <4>
            print(entry, end='') 
print()

