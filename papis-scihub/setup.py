# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as fd:
    long_description = fd.read()

setup(
    name='papis-scihub',
    version='1.3.0',
    author='Alejandro Gallo',
    author_email='aamsgallo@gmail.com',
    license='GPLv3',
    url='https://github.com/papis/scripts/tree/master/papis-scihub',
    install_requires=[
        "papis>=0.9",
        "python-doi>=0.1.0",
        "scihub>=0.0.1",
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    description='Scihub compatibility package for papis',
    long_description=long_description,
    keywords=[
        'papis', 'scihub', 'bibtex',
        'management', 'cli', 'biliography'
    ],
    packages=[
        "papis_scihub",
    ],
    entry_points={
        'papis.importer': [
            "scihub=papis_scihub.plugin:Importer",
        ],
    },
    platforms=['linux', 'osx'],
)
