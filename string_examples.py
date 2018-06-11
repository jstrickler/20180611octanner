#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'


print("It's a small world")
print('The "fix" is in')
print("""It's a "small" world""")

query = """
select *
from animals 
where species = 'wombat'
"""

#  \n \t \r \b \f
#  \xHH \000
#  \uHHHH \UHHHHHHHH
#  \N{degree symbol}

print("98\N{DEGREE SIGN} in SLC")
print("98\u00B0 in SLC")

cave_man = 'Barney Rubble'
print(len(cave_man))
# print(cave_man.__len__())
print(cave_man.upper())
print(cave_man.count('b'))

print(cave_man.lower().count('b'))

data = 'aardvark:bruin:catamount'

fields = data.split(':')
print(fields)

new_data = '<=>'.join(fields)
print(new_data)

s = "    All my exes live in Texas    "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = "xyxxyyxyxxxyyAll my exes live in Texasyxxyxxy"
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()
