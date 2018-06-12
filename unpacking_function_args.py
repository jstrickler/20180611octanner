#!/usr/bin/env python
# (c) John Strickler 2018

def foo(x, *y):
    print("x:", x)
    print("y:", y)

foo('a', 'b', 'c', 'd')
foo('a')

args = ['one', 'two', 'three']

foo('m', *args)

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

config(user='lagspike', color='orange')

info = {'user': 'Bob', 'color': 'purple'}

config(**info)
