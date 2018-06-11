#!/usr/bin/env python

class Rabbit:
    LOCATION = "the Cave of Caerbannog" # <1>

    def __init__(self, weapon):
        self.weapon = weapon
        
    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".
              format(self.LOCATION, self.weapon))  # <2>

r1 = Rabbit("a nice cup of tea")
r1.display() # <3>

r1 = Rabbit("big pointy teeth")
r1.display() # <3>
