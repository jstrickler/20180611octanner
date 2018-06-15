#!/usr/bin/env python

import requests

response = requests.get("http://www.python.org")

if response.status_code == requests.codes.OK:
    print(response.content.decode())
print()

for header, value in response.headers.items():
    print(f"{header:20.20} {value}")
