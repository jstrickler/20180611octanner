#!/usr/bin/env python

import sys
import os.path

if sys.platform == 'win32':
    user_key = 'USERNAME'
else:
    user_key = 'USER'

count_key = 'COUNT'

os.environ[count_key] = "42"  # <1>
print("count is",os.environ[count_key],"user is",os.environ[user_key]) # <2>
print("count is",os.environ.get(count_key),"user is",os.environ.get(user_key)) # <3>
user = os.getenv(user_key)  # <4>
count = os.getenv(count_key)
print("count is",count,"user is",user)
cmd = "count is ${} user is ${}".format(count_key, user_key)
print("cmd:", cmd)
print(os.path.expandvars(cmd)) # <5>

