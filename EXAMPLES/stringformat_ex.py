#!/usr/bin/env python

from datetime import date

color = 'blue'
animal = 'iguana'
place = 'ceiling'

#                0  1                            0
print('A lovely {} {} is on the {}'.format(color,animal, place)) # <1>

print('{0} {0} {0}'.format(animal))



fahr = 98.6839832
print('{:.1f}'.format(fahr)) # <2>

value = 12345
print('{0:d} {0:04x} {0:08o} {0:016b}'.format(value)) # <3>

data = {'A': 38, 'B': 127, 'C': 9}

for letter, number in sorted(data.items()):
    print("{} {:4d}".format(letter, number)) # <4>

thing = 'spam'

print("|{:10s}|".format(thing))
print("|{:<10s}|".format(thing))
print("|{:>10s}|".format(thing))
print("|{:^10s}|".format(thing))

print(thing)
