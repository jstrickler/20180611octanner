#!/usr/bin/env python
from sh import ls, who, df # <1>


ls('-l', '../DATA') # <2>
print('-' * 50)

w = who()  # <3>
print(w)
print('-' * 50)

diskfull = df('-h') # <4>
print(diskfull)
