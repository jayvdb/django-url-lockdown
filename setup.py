#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from setuptools import setup, find_packages


with open('README.md') as rme:
    readme = rme.read()
    description = readme

with open('requirements.txt') as req:
    requirements = req.readlines()


setup(
    name="django-url-lockdown",
    version='0.0.1',
    url='https://github.com/rangertaha/django-url-lockdown',
    author='Rangertaha',
    author_email='rangertaha@gmail.com',
    description=description,
    long_description=readme,
    packages=find_packages(exclude=['example', ]),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Framework :: Django',
    ],
)
