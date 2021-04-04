#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#from distutils.core import setup
from setuptools import setup, find_packages, Extension
import glob

VERSION = '0.1.10'

tests_require = []


def requirements():
    with open('requirements.txt', 'r') as fileobj:
        requirements = [line.strip() for line in fileobj]
        return requirements


setup(
    name='tuya-iot-app-sdk-python',
    url='https://github.com/tuya/tuya-iot-app-sdk-python',
    author="Tuya Inc.",
    author_email='developer@tuya.com',
    keywords='tuya iot app sdk python',
    description='Tuya IoT App SDK Python Version',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta'
        'License :: OSI Approved :: MIT License'
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    version=VERSION,
    install_requires=requirements(),
    tests_require=tests_require,
    test_suite='runtests.runtests',
    extras_require={'test': tests_require},
    entry_points={'nose.plugins': []},
    packages=find_packages(),
    python_requires='>=3.0',

)