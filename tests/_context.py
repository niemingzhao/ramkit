# -*- coding: utf-8 -*-

__all__ = []

import os
import sys

from setuptools import find_packages

sys.path.insert(0, os.path.abspath('..'))

for package in find_packages(exclude=['tests']):
    locals()[package] = __import__(package)
    __all__.append(package)
