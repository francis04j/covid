#!/usr/bin/env python

from distutils.core import setup

setup(name='Covid19DataApi',
      version='1.0',
      description='Covid19 Worldwide Data API',
      author='Francis Adediran',
      author_email='francis@francisade.com',
      url='https://francisade.com/',
      packages=['prometheus_client', 'requests', 'Flask'],
     )