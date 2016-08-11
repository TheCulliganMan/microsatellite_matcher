
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='microsatellite_matcher',
    version='0.0.1',
    description='microsatellite_matcher package for Python-Guide.org',
    long_description=readme,
    author='Ryan Culligan',
    author_email='rrculligan@gmail.com',
    url='https://github.com/TheCulliganMan/microsatellite_matcher',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
