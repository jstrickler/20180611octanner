#!/usr/bin/env python
from sh import tr

fruits = 'apple\nbanana\nmango\norange' # <1>

print(tr("[:lower:]", "[:upper:]", _in=fruits)) # <2>
