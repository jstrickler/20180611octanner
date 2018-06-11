#!/usr/bin/env python

import os

path = os.getenv('PATH')
paths = path.split(os.pathsep)

for path_dir in paths:
    if os.path.exists(path_dir):
        all_files = os.listdir(path_dir)
        print("{0}: {1}".format(path_dir, len(all_files)))
    else:
        print("WARNING: {} is in PATH, but does not exist".format(path_dir))
