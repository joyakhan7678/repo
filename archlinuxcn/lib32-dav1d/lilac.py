#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_provides(['libdav1d.so'])

def post_build():
    aur_post_build()
