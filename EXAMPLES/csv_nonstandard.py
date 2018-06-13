#!/usr/bin/env python
import csv

with open('../DATA/computer_people.txt') as computer_people_in:
    rdr = csv.DictReader(computer_people_in, delimiter=';',
                         fieldnames=['firstname', 'lastname', 'product']) # <1>

    for row in rdr:  # <2>
        print(row)

