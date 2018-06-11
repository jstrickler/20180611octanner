#!/usr/bin/env python
# (c) John Strickler 2018

#  for while

while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    if name == '':
        continue
    print("Hello,", name)
