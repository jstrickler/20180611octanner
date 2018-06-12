#!/usr/bin/env python
# (c) John Strickler 2018
fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(f):
    return f.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=str.lower)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

def kustom(fruit):
    return len(fruit), fruit.lower()

f5 = sorted(fruits, key=kustom)
print("f5:", f5, '\n')

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
print()

def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, product in sorted(people,
                     key=by_last_name):
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product in sorted(people,
                     key=lambda p: (p[1], p[0])):
    print(first_name, last_name)
print()


f6 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print("f6:", f6, '\n')
