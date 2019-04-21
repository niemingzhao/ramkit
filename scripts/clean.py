#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

print('=============================CLEAN====================================')

for root, dirs, files in os.walk(os.getcwd()):
    if root.startswith(os.path.abspath('venv')):
        continue
    for name in filter(lambda x: x == '__pycache__', dirs):
        shutil.rmtree(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: root == os.getcwd() and x == 'build', dirs):
        shutil.rmtree(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: root == os.getcwd() and x == 'dist', dirs):
        shutil.rmtree(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: x.endswith('.egg-info'), dirs):
        shutil.rmtree(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: x.endswith('.pyc'), files):
        os.remove(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: x.endswith('.pyo'), files):
        os.remove(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: x.endswith('.pyd'), files):
        os.remove(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: x.endswith('.spec'), files):
        os.remove(os.path.abspath(os.path.join(root, name)))
    for name in filter(lambda x: x.endswith('.log'), files):
        os.remove(os.path.abspath(os.path.join(root, name)))
