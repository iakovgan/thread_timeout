#!/usr/bin/python
from setuptools import setup, find_packages

import re
# hacky way to get __version__ from __init__
# we can not just import since some dependancies could be not installed yet 
metadata = dict(re.findall("\n__([a-z]+)__ = '([^']+)'", open('hostsync/__init__.py').read()))
__version__ = metadata['version'] 

setup(
    name='thread_timeout',
    version=__version__,
    description='''Decorator to execute functionin in separate thread with timeout''',
    author='George Shuklin',
    author_email='george.shuklin@gmail.com',
    url='https://github.com/amarao/thread_timeout',
    packages=find_packages(),
    install_requires=['wrapt'],
    license='LGPL',
    classifiers=[
         "Development Status :: 4 - Beta",
         "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
         "Topic :: Software Development :: Libraries",
    ],
)
