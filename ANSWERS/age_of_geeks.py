#!/usr/bin/env python
# (c)2015 John Strickler

import openpyxl as px

wb =px.load_workbook('../DATA/computer_people.xlsx')

ws = wb.get_sheet_by_name('people')

age_total = 0
num_people = 0
for row in ws['A2:D9']:
    age = row[3].value
    if isinstance(age, int):
        age_total += age
        num_people += 1

avg_age = age_total/num_people
print(("Average age is {}".format(avg_age)))
