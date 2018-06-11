#!/usr/bin/env python

colors = [ 'red', 'green', 'blue', 'purple', 'pink', 'yellow', 'black' ]  # <1>

for color in colors:  # <2>
    print(color)
print()

with open('../DATA/mary.txt') as MARY:  # <3>
    for line in MARY:    # <4>
        print(line,end='')  # <5>
print()

while True:  # <6>
    name = input("What is your name? ")  # <7>
    if name.lower() == 'q':
       break  # <8>
    print("Welcome,",name)
