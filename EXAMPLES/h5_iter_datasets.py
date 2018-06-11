#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

H5_DATASET = '/arrays/2D int8x9'

hfile = h5py.File(H5_FILE) # <1>

dset = hfile[H5_DATASET]  # <2>

for i, row in enumerate(dset):  # <3>
    print("ROW {}: {}".format(i, row)) # <4>
print()

print("Row 1:")
print(dset[1])  # <5>
print()


print("Column 1:")
print(dset[:,1])
print()

print("Rows 3 & 4, Columns 5 & 6")
print(dset[3:5, 5:7])

