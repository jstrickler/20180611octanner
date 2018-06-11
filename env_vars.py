#!/usr/bin/env python
# (c) John Strickler 2018
import os

print(os.getenv('TERM_PROGRAM'))
print(os.getenv('USER'))
print(os.getenv('ROCK_BAND'))
print(os.getenv('ANIMAL', 'wombat'))
