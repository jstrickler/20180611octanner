#!/usr/bin/env python
# (c) John Strickler 2018

with open('DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(line, end='')
print()
mary_in = open('DATA/mary.txt')
for line in mary_in:
    print(line, end='')
mary_in.close()
print()

colors = ['green', 'red', 'blue', 'purple']

for i, color in enumerate(colors):
    print(i, color)
print()

e = enumerate(colors)
print(e)
print(list(e), '\n')

e = enumerate(colors)
for i, color in e:
    print(i, color)


