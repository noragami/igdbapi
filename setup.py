#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()


setup(name='igdbapi',
      version='0.2',
      description='An object-oriented Python 2.7+ library for accessing the Igdb API',
      url='https://github.com/noragami/igdbapi',
      author='noragami',
      author_email='yuumeikai@gmail.com',
      license='MIT',
      packages=['igdbapi'],
      download_url='https://github.com/noragami/igdbapi/tarball/0.2',
      keywords=['igdb', 'api', 'games'],
      classifiers=[],
      install_requires=requirements,
      zip_safe=False)
