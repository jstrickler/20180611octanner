#!/usr/bin/env python

import re
from collections import Counter

RX = r'\W+'

with open("../DATA/mary.txt") as mary_in:
    all_words = [w.lower()  for ln in mary_in  for w in re.split(RX, ln) if w != ''] #<1>

print("all words:", all_words, '\n')

mary_unique = set(all_words)
print(mary_unique, '\n')

mary_count = Counter(all_words) # special dict
print(mary_count.most_common(5), '\n')
print("mary_count as list:", list(mary_count.items()), '\n')


greater = [(word, count) for word, count in mary_count.items() if count > 1]
print(greater, '\n')

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'SLC': 'Salt Lake City',
    'IAD': 'Dulles',
}

for code, name in airports.items():
    print(code, "is", name)

print(list(airports.items()))
