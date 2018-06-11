#!/usr/bin/env python

import os
'''print size of every python file whose name starts with "m" '''

START_DIR = ".."   # start in root of student files  # <1>

def main():
    for currdir,subdirs,files in os.walk(START_DIR): # <2>
        for file in files: # <3>
            if file.endswith('.py') and file.startswith('m'):
                fullpath = os.path.join(currdir,file) # <4>
                fsize = os.path.getsize(fullpath)
                print("{:8d} {:s}".format(fsize, fullpath))

if __name__ == '__main__':
    main()
