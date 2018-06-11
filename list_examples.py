#!/usr/bin/env python

list1 = list()
list2 = ['a', 'b', 'c']
list3 = []
list4 = 'a b c'.split()

fruits = ['lemon', 'pomegranate', 'mulberry']
fruits.append('kiwi')
print(fruits)
fruits.insert(0, 'lime')
fruits.insert(4, 'durian')
print(fruits)
fruits.insert(27, 'apple')
print(fruits)
fruits.extend(['raspberry', 'banana'])
print(fruits)
fruits.append(['cherry', 'peach'])
print(fruits)

del fruits[-1]
# del fruits[len(fruits)-1]

print(fruits)

fruits.remove('durian')
print(fruits)

x = fruits.pop()
print(x)
print(fruits)

y = fruits.pop(2)
print(y)
print(fruits)
print()

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(fruits[0:3])   # start:stop
#  start is INclusive
#  stop is EXclusive  (limit/sentinel)
print(fruits[4:8])
print(fruits[:3])
print(fruits[10:])
print(fruits[10:len(fruits)])
print(fruits[::2])
print(fruits[::])

city = "Salt Lake City"

print(city[:4])
print(city[5:9])
print(city[-4:])

print(city[:-5])


