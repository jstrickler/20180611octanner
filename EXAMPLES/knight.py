#!/usr/bin/env python

class Knight(object):
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self._color = color

    @property  # <1>
    def name(self):  # <2>
        return self._name

    @property
    def color(self):
        return self._color

    @color.setter  # <3>
    def color(self, color):
        self._color = color

    @property
    def title(self):
        return self._title


if __name__ == '__main__':
    k = Knight("Lancelot", "Sir", 'blue')

    # Bridgekeeper's question
    print('Sir {}, what is your...favorite color?'.format( k.name )) # <4>

    # Knight's answer
    print("red, no -- {}!".format( k.color ))

    k.color = 'red' # <5>

    print("color is now:", k.color)
