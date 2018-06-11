#!/usr/bin/env python

fruits = ['watermelon','Apple','Mango','KIWI','apricot','LEMON','guava']

sfruits = sorted(fruits,key=lambda e: e.lower()) # <1>

print(" ".join(sfruits))

