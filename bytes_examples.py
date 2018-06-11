#!/usr/bin/env python

with open('DATA/salad.gif', 'rb') as salad_in:
    data = salad_in.read()

print(type(data))

s = "foo\u00B0\n"  #  seq of CHARs
b = b"bar\n"  # seq of BYTEs

print(s.encode())
print(b.decode())
