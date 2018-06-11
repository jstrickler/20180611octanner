#!/usr/bin/env python

from sh import ls, glob # <1>

print(ls('-ld', glob('/etc/pr*'))) # <2>
