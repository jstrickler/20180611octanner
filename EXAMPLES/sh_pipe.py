#!/usr/bin/env python
from sh import grep, netstat


print(grep(netstat('-an'), 'LISTEN'))  # <1>
