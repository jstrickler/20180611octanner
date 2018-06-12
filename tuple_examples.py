#!/usr/bin/env python
# (c) John Strickler 2018


p2 = ['Tom', 'Bombadil', 45]  # list

p3 = {'Tom', 'Bombadil', 45}  # set

p4 = {'firstname': 'Tom', 'lastname': 'Bombadil', 'age': 45} # dict

person = 'Tom', 'Bombadil', 45 # tuple
print(type(person))
print(person[0], person[1])

first_name, last_name, age = person # iterable unpacking
print(first_name, last_name)

def get_person():
    return 'Tom', 'Bombadil', 45

first_name, last_name, age = get_person()
print(first_name, last_name)

person = get_person()
print(person[0], person[1])

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google', 'ABC'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'git'),
    ('John', 'Strickler'),
]

for first_name, last_name, *product in people:
    print(first_name, last_name, product)
print('-' * 60)


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

