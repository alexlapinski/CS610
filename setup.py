# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CS610',
    version='0.1.0',
    description='Collection of algorithms for CS610.',
    long_description=readme,
    author='Alex Lapinski',
    author_email='contact@alexlapinski.name',
    url='https://github.com/alexlapinski/CS610',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
