# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 23:39:14 2019

@author: david
"""

import os
from tinytag import TinyTag
path = os.getcwd()
print(path)
for fpath, dirname, fnames in os.walk(path):
    print(fpath)