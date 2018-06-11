#!/usr/bin/env python
from sh import ls # <1>


ls('-l', '../DATA',  _bg=True,   _out='ls_out.txt')  # <2> <3>
print("Done.")
