#!/usr/bin/env python

import threading
import random
import time

class SimpleThread(threading.Thread):
    def __init__(self,num):
        super().__init__()  # <1>
        self._threadnum =num
    
    def run(self): # <2>
        time.sleep(random.randint(1,10))
        print("Hello from thread {}".format(self._threadnum))

for i in range(10):
    t = SimpleThread(i) # <3>
    t.start() # <4>

print("Done.")

