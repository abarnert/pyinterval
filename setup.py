#! /usr/bin/env python

# Copyright (c) 2015, Andrew Barnert <abarnert@yahoo.com>
# Copyright (c) 2008, Stefano Taschini <taschini@ieee.org>
# All rights reserved.
# See LICENSE for details.

"""Script for setting the distribution of the interval package and the
crlibm extension.

Typical usage
-------------

Build crlibm and place it in the current directory:

    python setup.py build_ext -i


Create a source distribution:

    python setup.py sdist --formats=gztar,zip

"""


try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
from distutils.command.build_py import build_py

# A subset of http://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: C',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2',
    'Topic :: Scientific/Engineering :: Mathematics'
]

metadata = dict(
    description  = 'Interval arithmetic in Python',
    author       = 'Andrew Barnert',
    author_email = 'abarnert@yahoo.com',
    url          = "https://github.com/abarnert/pyinterval/",
    classifiers  = classifiers
);

setup(
    name         = 'pyinterval',
    version      = '1.1',
    use_2to3     = True,
    packages     = ['interval'],
    ext_modules  = [
        Extension(
            'interval.crlibm',
            sources      = ['ext/crlibmmodule.c'],
            include_dirs = ['/opt/crlibm/include'],
            library_dirs = ['/opt/crlibm/lib'],
            libraries    = ['crlibm'])
        ],
    **metadata)
