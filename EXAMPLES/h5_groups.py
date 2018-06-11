#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

with h5py.File(H5_FILE) as hfile: # <1>

    print('groups:')
    for group in hfile:  # <2>
        print(group)
    print()

    print('datasets in /arrays:')
    for dataset in hfile['arrays']: # <3>
        print(dataset)

    print('-' * 60)
    print("Group/Dataset tree:")
    for obj_name in hfile:  # <2>
        print(obj_name)
        obj = hfile[obj_name]  # <4>
        if isinstance(obj, h5py.Group):
            for item_name in obj:  # <5>
                item = obj[item_name] # <6>
                item_type = type(item).__name__ # <7>
                print('\t{} ({})'.format(item_name, item_type))
        else:
            obj_type = type(obj).__name__ # <7>
            print('\t{} ({})'.format(obj_name, obj_type))

