#!/usr/bin/env python
import re
from glob import glob

files = glob('*.eml')

for file_name in files:
    with open(file_name, 'rb') as file_in:
        content = file_in.read()
        for m in re.findall(b'\d{3}\d+\d{2}\d+\d{4}'):
            print(file_name, m.start(0), m.group(0))
