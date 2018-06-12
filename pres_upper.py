#!/usr/bin/env python
# (c) John Strickler 2018

presidents = []

with open('DATA/presidents.txt') as pres_in:
    for line in pres_in:
        presidents.append(line.rstrip().split(':'))
print(presidents)

pres_upper = [f"{p[2]} {p[1]}".upper() for p in presidents]
print(pres_upper, '\n')
print('-' * 60)

potus_tuples = []
for p in presidents:
    potus_tuples.append( (p[2], p[1], p[3], p[-1]) )

for pres in sorted(potus_tuples, key=lambda p: p[2]):
    print(pres)
