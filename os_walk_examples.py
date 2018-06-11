#!/usr/bin/env python
# (c) John Strickler 2018
import os

TARGET_DIR = '.'

for curr_dir, dir_list, file_list in os.walk(TARGET_DIR):
    if 'git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print('  {:8d} {}'.format(file_size, file_name))
print('-' * 60)

for x in os.walk('/tmp'):
    print(x)
