#!/usr/bin/env python
# (c) John Strickler 2018
from collections import namedtuple

person = "Fred", "Moore", 55

print(person[0])

person = {
    'firstname': 'Fred', 'lastname': 'Moore', 'Age': 55
}

print(person['firstname'])


Person = namedtuple("Person", 'firstname lastname age')


p1 = Person('Fred', 'Moore', 55)
p2 = Person('Mary', 'Gonzalez', 42)

print(p1.firstname, p1.lastname, '\n')

print(dir(p1), '\n')

print(p1._asdict())

x = p1._replace(firstname='Bob')
print(x)

import collections as co

x = co.namedtuple('x', 'x y z')

from collections import namedtuple as nt

y = nt('y', 'a b c')


Wombat = namedtuple('Wallaby', 'a b c')

w = Wombat(1, 2, 3)
print(w.a, w.b)
print(type(w))

