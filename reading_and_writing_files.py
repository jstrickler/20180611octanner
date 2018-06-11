#!/usr/bin/env python
# (c) John Strickler 2018

with open('DATA/computer_people.txt') as cp_in:
    for raw_person in cp_in:
        person = raw_person.rstrip()
        fields = person.split(';')
        if fields[0].startswith('L'):
            print(fields)
print()

with open('DATA/computer_people.txt') as cp_in:
    all_contents = cp_in.read()
    print(all_contents)
print()

with open('DATA/computer_people.txt') as cp_in:
    all_lines = cp_in.readlines()
    print(all_lines)

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitdata.txt', 'w') as fruitdata_out:
    for fruit in fruits:
        fruitdata_out.write(fruit + '\n')
