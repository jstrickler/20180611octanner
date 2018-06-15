#!/usr/bin/env python

import urllib.request  # <1>

with urllib.request.urlopen("http://www.python.org") as response:  # <2>
    print(response.info())  # <3>
    print("-" * 60)

    print(response.read().decode())  # <4> <5>
