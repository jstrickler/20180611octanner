#!/usr/bin/env python
# (c) John Strickler 2018
import re

bad_text = b"awoeifj awoefj awo\x011\x14\x1eifj awoiefj"

print(bad_text)
print(bad_text.decode())

RX = rb'[^ -~]'

print(re.sub(RX, b'', bad_text))
