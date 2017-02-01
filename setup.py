#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def local_requirements():
    req_list = []
    with open('requirements.txt') as requirements_file:
        req_list = [line.strip() for line in requirements_file.readlines()]
    install_reqs = list(filter(None, req_list))
    return install_reqs


setup(name='igdbapi',
      version='0.1',
      description='An object-oriented Python 2.7+ library for accessing the Igdb API',
      url='https://github.com/noragami/igdbapi',
      author='noragami',
      author_email='yuumeikai@gmail.com',
      license='MIT',
      packages=['igdbapi'],
      install_requires=local_requirements(),
      zip_safe=False)
