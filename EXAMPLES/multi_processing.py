#!/usr/bin/env python

import random
from multiprocessing import Manager, Lock, Process, Queue, freeze_support
from queue import Empty
import time

NUM_ITEMS = 25000 # <1>
POOL_SIZE = 100

class RandomWord(object):  # <2>
    def __init__(self):
        with open('../DATA/words.txt') as WORDS:
            self._words = [word.rstrip('\n\r') for word in WORDS]
        self._num_words = len(self._words)

    def __call__(self): # <3>
        return self._words[random.randrange(0, self._num_words)]

class Worker(Process):  # <4>

    def __init__(self, name, q, result_lock, result):  # <5>
        Process.__init__(self)
        self.q = q
        self.result = result
        self.result_lock = result_lock
        self.name = name

    def run(self):  # <6>
        while True:
            try:
                s1 = self.q.get(block=False)  # <7>
                s2 = s1.upper()  # <8>
                with self.result_lock:
                    self.result.append(s2)  # <9>

            except Empty:  # <10>
                break

if __name__ == '__main__':
    q = Queue()  # <11>

    manager = Manager()  # <12>
    shared_result = manager.list()  # <13>
    result_lock = Lock()  # <14>

    random_word = RandomWord() # <15>
    for i in range(NUM_ITEMS):
        w = random_word()
        q.put(w)  # <16>
    
    start_time = time.ctime()
    
    pool = [] # <17>
    for i in range(POOL_SIZE): # <18>
        name = "Worker {:03d}".format(i)
        w = Worker(name, q, result_lock, shared_result)  # <19>
        #
        w.start() # <20>
        pool.append(w) # <21>
        
    for t in pool:
        t.join() # <22>
    
    end_time = time.ctime()
    
    print((shared_result[-50:]))  # <23>
    print(len(shared_result))
    print(start_time)
    print(end_time)
