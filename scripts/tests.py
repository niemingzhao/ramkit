#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import doctest
import os

from setuptools import find_packages

print('============================DOCTEST===================================')

for package in find_packages(exclude=['tests']):
    for root, dirs, files in os.walk(package):
        for name in filter(lambda x: x.endswith('.py'), files):
            name = os.path.abspath(os.path.join(root, name))
            doctest.testfile(name, module_relative=False, verbose=True)

print('============================UNITTEST==================================')

os.system('python -m unittest discover -v')
