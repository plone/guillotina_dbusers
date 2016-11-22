# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name='pserver.zodbusers',
    version=open('VERSION').read().strip(),
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGELOG.rst').read()),
    classifiers=[
        'Framework :: Plone :: 7.0',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='https://pypi.python.org/pypi/pserver.zodbusers',
    license='GPL version 3',
    setup_requires=[
        'pytest-runner',
    ],
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['pserver'],
    install_requires=[
        'setuptools',
        'plone.server'
    ],
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest',
            'requests',
            'zope.testing'
        ]
    },
    entry_points={
        'plone.server': [
            'include = pserver.zodbusers',
        ]
    }
)
