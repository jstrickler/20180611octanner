#!/usr/bin/env python
# (c) John Strickler 2018
import os

os.system("hostname")

with os.popen("hostname") as hostname_in:
    hostname = hostname_in.read().rstrip()

print(hostname)
