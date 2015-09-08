#!/usr/bin/python
import os.path
import codecs
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='thread_timeout',
    version="0.1",
    description='''Decorator to execute functionin in separate thread with timeout''',
    long_description=read("README.rst"),
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
