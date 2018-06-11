#!/usr/bin/env python

from sh import netstat

ns = netstat.bake('-an')  # <1>

print(ns()) # <2>

