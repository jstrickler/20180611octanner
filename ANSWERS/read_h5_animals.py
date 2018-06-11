#!/usr/bin/env python
import h5py

H5_FILE = '../DATA/h5/example.h5'

H5_DATASET = '/Animals/observations'

hfile = h5py.File(H5_FILE)

dset = hfile[H5_DATASET]

for row in dset:
    print("{:3.0f} {:12.5f}".format(*row))


