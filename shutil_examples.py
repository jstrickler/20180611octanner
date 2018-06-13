#!/usr/bin/env python
# (c) John Strickler 2018
import shutil
from contextlib import suppress


shutil.copy('set_examples.py', '/tmp')
with suppress(FileNotFoundError):
    shutil.rmtree('foo')

shutil.make_archive('DATA', 'zip' )
shutil.make_archive('DATA', 'gztar' )
