#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='SocialApp',
      version='1.0',
      description='Sommercamp 2023 Social Media App',
      author='Isabella Graßl',
      author_email='isabella.grassl@uni-passau.de ',
      packages=find_packages(),
      scripts=['manage.py']
      )
