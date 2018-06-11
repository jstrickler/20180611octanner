#!/usr/bin/env python
import sh

print(sh.ls('-l','../DATA')) # <1>
print('-' * 50)

w = sh.who()  # <2>
print(w)
print('-' * 50)

diskfull = sh.df('-h')  # <3>
print(diskfull)
