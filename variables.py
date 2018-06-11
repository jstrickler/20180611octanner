#!/usr/bin/env python
import copy

a = 10
b = 42
c = a
a = 50
print(a, c)
d = 10
a = 11

del a

_ = 5

print(_)


customer_last_name = 'Smith'

things = ['wombat', 42, 'meerkat']
stuff = things
stuff = []
stuff.append('bandicoot')
stuff.extend(things)
print('things:', things)
print('stuff:', stuff)

x = list(things)   # shallow
y = copy.deepcopy(things)  # deep

data = [
    ['a', 'b', 'c'],
    [1, 2, 3],
]

print(data[0])
print(data[1])
print(data[0][0])
d1 = data
d2 = list(data)
print("d2:", d2)
print(id(d1), id(d2))
d2[0].append('d')
print(d1)
d3 = copy.deepcopy(data)
d3[0].append('wombat')
print("d1:", d1)
print("d3:", d3)
