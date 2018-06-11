#!/usr/bin/env python

import queue
import random
from threading import Thread,Lock as tlock
import time

NUM_ITEMS = 25000
POOL_SIZE = 100

q = queue.Queue(0) # <1>

shared_list = []
shlist_lock = tlock() # <2>
stdout_lock = tlock() # <2>

import random

class RandomWord(object): # <3>
    def __init__(self):
        with open('../DATA/words.txt') as WORDS:
            self._words = [word.rstrip('\n\r') for word in WORDS.readlines()]
        self._num_words = len(self._words)
        
    def __call__(self):
        return self._words[random.randrange(0,self._num_words)]

class Worker(Thread): # <4>
    
    def __init__(self,name): # <5>
        Thread.__init__(self)
        self.name = name
    
    def run(self): # <6>
        while True:
            try:
                s1 = q.get(block=False) # <7>
                s2 = s1.upper() + '-' + s1.upper()
                with shlist_lock: # <8>
                    shared_list.append(s2)

            except queue.Empty: # <9>
                break

# <10>
random_word = RandomWord()
for i in range(NUM_ITEMS):
    w = random_word()
    q.put(w)

start_time = time.ctime()

# <11>
pool = []
for i in range(POOL_SIZE):
    name = "Worker {:c}".format(i+65)
    w = Worker(name)  # <12>
    w.start() # <13>
    pool.append(w)
    
for t in pool:
    t.join() # <14>

end_time = time.ctime()

print(shared_list[:20])

print(start_time)
print(end_time)

