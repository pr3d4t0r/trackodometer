#!/usr/bin/env python3
# See: https://github.com/pr3d4t0r/trackodometer/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


import sys

from setuptools import find_packages
from setuptools import setup


# *** functions ***

def readToList(fileName):
    return [line.strip() for line in open(fileName).readlines()]


# *** main ***

if '__main__' == __name__:
    requirements = readToList('requirements.txt')

    setup(
        author               = 'pr3d4t0r',
        author_email         = 'trackodometer AT cime.net',
        description          = 'Tracking competition tools',
        include_package_data = True,
        install_requires     = requirements,
        license              = open('LICENSE.txt').read(),
        long_description     = open('README.md').read(),
        name                 = open('modulename.txt').read().replace('\n', ''),
        namespace_packages   = [ ],
        packages             = find_packages(),
        url                  = 'https://github.com/pr3d4t0r/trackodometer',
        version              = open('version.txt').read().strip(),
    )

sys.exit(0)


