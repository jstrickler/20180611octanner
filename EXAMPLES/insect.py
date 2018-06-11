#!/usr/bin/env python

from  animal import Animal

class Insect(Animal):
    '''
        An animal with 2 sets of wings and 3 pairs of legs
    '''
    def __init__(self, species, name, sound, can_fly=True): # <1>
        super().__init__(species, name, sound) # <2>
        self._can_fly = can_fly

    @property
    def can_fly(self): # <3>
        return self._can_fly

if __name__ == '__main__':
    mon = Insect('monarch butterfly', 'Mary', None) # <4>
    scar = Insect('scarab beetle', 'Rupert', 'Bzzz', False)

    for insect in mon, scar:
        flying_status = 'can' if insect.can_fly else "can't"
        print("Hi! I am {} the {} and I {} fly!".format( # <5>
                insect.name, insect.species, flying_status
            ),
        )
        insect.make_sound() # <6>
        print()
