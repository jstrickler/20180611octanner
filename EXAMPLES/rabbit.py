#!/usr/bin/env python

class Rabbit: 

    def __init__(self,size,danger): # <1>
        self._size = size
        self._danger = danger 
        self._victims = []

    def threaten(self): # <2>
        print("I am a {} bunny with {}!".format(self._size, self._danger))

r1 = Rabbit('large',"sharp, pointy teeth")  # <3>
r1.threaten() # <4>

r2 = Rabbit('small','fluffy fur')
r2.threaten()




