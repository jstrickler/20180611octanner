#!/usr/bin/env python
import re
from glob import glob

files = glob('*.eml')

RX_SSN = r'\b\d{3}[^\d\w\s]?\d{2}[^\d\w\s]?\d{4}\b'

for file_name in files:
    with open(file_name, 'r') as file_in:
        content = file_in.read()
        for m in re.finditer(RX_SSN, content):
            print(file_name, m.start(0), m.group(0))
