#!/usr/bin/env python
# (c) John Strickler 2018
from octlib import encourage, reward, Trophy
import sys

encourage()
reward()

t = Trophy()

for path in sys.path:
    print(path)
