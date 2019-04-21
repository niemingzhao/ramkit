#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('=============================DOCS=====================================')

reply = input('> Rerun autodoc to insert docstrings from modules (y/N) [n]:')
if reply == 'y':
    os.system('sphinx-apidoc -P -f -o docs . tests setup.py')
os.system('cd docs && make clean && make html')
