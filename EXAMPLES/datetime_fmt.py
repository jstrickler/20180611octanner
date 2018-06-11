#!/usr/bin/env python
from datetime import datetime as DateTime

# Bill Gates's birthday
gates_bd = DateTime(1955,10,28, 22, 0, 0) # <1>

print(gates_bd) # <2>
print()

print(gates_bd.strftime('Bill was born on %B %d, %Y at %I:%M %p')) # <3>
print()

print(gates_bd.strftime('BG: %m/%d/%y')) # <3>
print()

print(gates_bd.strftime('Mr. Gates was born %d-%b-%Y')) # <3>
print()

print(gates_bd.strftime('log entry: %Y-%m-%d')) # <3>
print()
