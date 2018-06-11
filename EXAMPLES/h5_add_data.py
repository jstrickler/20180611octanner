#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

with h5py.File(H5_FILE) as hfile:  # <1>
    ds1 = hfile.create_dataset('/Animals/wombat', (15, 2))  # <2>
    ds2 = hfile.create_dataset(
        '/Animals/bushbaby', (100, 3), dtype='i8' # <3>
    )

