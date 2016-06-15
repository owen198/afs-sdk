#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(
    name='helloworld',
    version='2.0',
    description='Simple module helloworld.say()',
    long_description=open('README').read(),
    author='Wang Diwen',
    author_email='wangdiwen521@gmail.com',
    url='https://github.com/wangdiwen',
    license='MIT',
    install_requires=['setuptools'],
    packages=['helloworld'],
)
