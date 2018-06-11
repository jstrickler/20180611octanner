#!/usr/bin/env python
class AnimalBase():  # <1>
    def __init__(self, name):
        self._name = name

    def id(self):
        print(self._name)

class CanBark():  # <2>
    def bark(self):
        print("woof-woof")

class CanFly(): # <2>
    def fly(self):
        print("I'm flying")


class Dog(CanBark, AnimalBase): # <3>
    pass

class Sparrow(CanFly, AnimalBase): # <3>
    pass

d = Dog('Dennis')
d.id()    # <4>
d.bark()  # <5>
print()

s = Sparrow('Steve')
s.id()
s.fly()  # <6>
print()

print("Sparrow mro:", Sparrow.mro())

