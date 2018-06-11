#!/usr/bin/env python
from sh import wc

count = wc('-l', '../DATA/words.txt')

print(count)
