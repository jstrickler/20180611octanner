#!/usr/bin/env python

import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # <1>

s.connect((socket.gethostname(),7777)) # <2>

if len(sys.argv) > 1:
   msg = sys.argv[1]
else:
   msg = "default message"

s.sendall(msg.encode())  # <3>

reply = s.recv(4096)  # <4>

print("Server said >{}<".format(reply.strip().decode())) # <5>

s.close() # <6>
