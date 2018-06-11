#!/usr/bin/env python
# (c) 2015 John Strickler
#
from collections import defaultdict
from pprint import pprint

fruits = ["pomegranate","cherry","apricot","date","apple","lemon","kiwi",
"orange","lime","watermelon","guava","papaya","fig","pear","banana",
"tamarind","persimmon","elderberry","peach","blueberry","lychee",
 "grape" ]

fruits_by_first_letter = defaultdict(list)   # <1>

for fruit in fruits:
    first_letter = fruit[0] # <2>

    fruits_by_first_letter[first_letter].append(fruit) # <3>


pprint(fruits_by_first_letter) # <4>
