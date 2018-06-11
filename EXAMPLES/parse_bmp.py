#!/usr/bin/env python

from struct import Struct

# short int short short int (native, unsigned)
s = Struct('=HIHHI') # <1>

with open('../DATA/chimp.bmp','rb') as CHIMP:
    chimp_bmp = CHIMP.read(14)  # <2>

(signature,size,reserved1,reserved2,offset) = s.unpack(chimp_bmp)  # <3>

print("signature:",signature)  # <4>
print('size:',size)
print('reserved1:',reserved1)
print('reserved2:',reserved2)
print('offset:',offset)
