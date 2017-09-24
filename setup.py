#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for joes-pizzeria"""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, 'CHANGELOG.rst'), 'r', encoding='utf-8') as changelog_file:
    changelog = changelog_file.read()

requirements = [
    'anyblok',
    'psycopg2',
    'anyblok_pyramid',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='joes_pizzeria',
    version='0.1.0',
    description="Sale application based on REA patterns",
    long_description=readme + '\n\n' + changelog,
    author="Simon ANDRE",
    author_email='sandre@anybox.fr',
    url='https://github.com/sandreanybox/joes-pizzeria',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'joes_pizzeria=joes_pizzeria.joes_pizzeria:Joes_pizzeria'
            ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='joes-pizzeria',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
