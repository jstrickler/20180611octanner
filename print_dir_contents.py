#!/usr/bin/env python

import os

def recurse_dir(path):
    print("DIR:", path)
    for node in os.listdir(path):
        if os.path.isdir(node):
            recurse_dir(node)
        else:
            print("FILE:", node)


def print_directory_contents(sPath):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    recurse_dir(sPath)

if __name__ == '__main__':
    print_directory_contents('.')
