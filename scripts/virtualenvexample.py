#!/usr/bin/env python

import os

path = os.path.expanduser(os.environ['PATH'])
print(path)

import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print(','.join(user_paths))

import sys
print(sys.version)
