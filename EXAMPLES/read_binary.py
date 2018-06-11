#!/usr/bin/env python

# print out a file 10 bytes at a time

with open("../DATA/parrot.txt", "rb") as parrot_in: # <1>
    while True:
        chunk = parrot_in.read(10)  # <2>
        if chunk == b"":   # <3>
            break
        print(chunk.decode()) # <4>
