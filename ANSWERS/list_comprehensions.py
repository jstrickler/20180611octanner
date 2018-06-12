#!/usr/bin/env python
# (c) John Strickler 2018

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

food = ['spam', 'spam', 'bacon', 'spam', 'spam', 'spam', 'eggs', 'spam', ]

nonspam = [f for f in food if f != 'spam']
print("nonspam:", nonspam, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = [n * 1000 for n in nums]
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print('last_names:', last_names, '\n')

suits = 'Clubs Diamonds Hearts Spades'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = ["{}-{}".format(r,s) for s in suits for r in ranks]
print('cards:', cards, '\n')
