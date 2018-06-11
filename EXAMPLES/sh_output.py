#!/usr/bin/env python
from sh import grep # <1>

grep('root','/etc/passwd',_out='grep.out') # <2>
