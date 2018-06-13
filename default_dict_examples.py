#!/usr/bin/env python
# (c) John Strickler 2018
from collections import defaultdict
from pprint import pprint

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

data = defaultdict(list)

for fruit in fruits:
    data[fruit[0]].append(fruit)

pprint(data)
print()

magic = defaultdict(lambda :0)

magic['red'] = 18
magic['ecru'] = 29
magic['orange'] = 50

print(magic)

print(magic['blue'])

print(magic)
