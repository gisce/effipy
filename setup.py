#!/usr/bin/env python
"""
effipy
======

Python library for the EffiPeople REST API.

:copyright: (c) 2013 by GISCE-TI, S.L., see AUTHORS for more details.
:license: MIT, see LICENSE for more details.
"""
from setuptools import setup, find_packages

tests_require = []

install_requires = [
    'libsaas',
]

setup(
    name='effipy',
    version='0.5.0',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    url='http://code.gisce.net/effipy',
    description='Python library for the Effipeople REST API.',
    long_description=__doc__,
    license='MIT',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='nose.collector',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
