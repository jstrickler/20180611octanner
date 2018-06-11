#!/usr/bin/env python
# (c) John Strickler 2018

data = ['a', 'b', 'c']

for d in data:
    print(d)

idata = iter(data)
while True:
    try:
        d = next(idata)
        print(d)
    except StopIteration:
        break

