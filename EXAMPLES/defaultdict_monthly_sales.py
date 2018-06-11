#!/usr/bin/env python
# (c) 2015 John Strickler
#
from collections import defaultdict


MONTHS = '''
    Jan Feb Mar Apr May Jun
    Jul Aug Sep Oct Nov Dec
'''.split()


sales_data = defaultdict(lambda: 0) # <1>

with open('../DATA/sales_by_month.txt') as sbm_in:
    for line in sbm_in:
        month, raw_sales = line.strip('\n\r').split('|')
        sales = int(raw_sales)
        sales_data[month] += sales # <2>

for month in MONTHS:
    print("{}: {:5d}".format(month, sales_data[month])) # <3>


