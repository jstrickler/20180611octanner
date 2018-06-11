#!/usr/bin/env python
# (c) John Strickler 2018
import os   # os.path
from datetime import datetime

print(dir(os))
print('-' * 60)

print(dir(os.path))

FOLDER = 'DATA'
FILE = 'mary.txt'

file_path = os.path.join(FOLDER, FILE)
print('file path:', file_path)

file_size = os.path.getsize(file_path)
print("file size:", file_size)

raw_file_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_file_timestamp)
file_timestamp = datetime.fromtimestamp(raw_file_timestamp)
print("file mod time:", file_timestamp)

print("folder:", os.path.dirname(file_path))
print("file only:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))

