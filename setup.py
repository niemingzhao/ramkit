#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

config = {
    'name': 'ramkit',  # Required
    'version': '0.0.1',  # Required
    'description': 'An analysis kernel for raman spectrum.',  # Required
    'long_description': """An analysis kernel for raman spectrum.""",
    'author': 'Nie Mingzhao',
    'author_email': '1432440963@qq.com',
    'url': 'https://github.com/niemingzhao/ramkit',
    'download_url': 'https://github.com/niemingzhao/ramkit/archive/master.zip',
    'keywords': 'raman spectrum spectroscopy algorithm',
    'platforms': 'any',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Physics'
    ],

    'packages': find_packages(exclude=['tests']),  # Required
    'include_package_data': True,
    'python_requires': '~=3.6',
    'install_requires': ['numpy',
                         'sympy',
                         'scipy',
                         'pandas',
                         'matplotlib',
                         'scikit-learn']
}

setup(**config)
