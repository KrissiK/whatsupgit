# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

from setuptools import setup

setup(name='whatsupgit',
      version='0.9',
      description='A tool that shows changes in your git repositories, that are spread over your filesystem',
      author='Kristin Kuche',
      author_email='kristin.kuche@gmx.net',
      packages=['whatsupgit'],
      install_requires=['pygit2==0.19',],
      zip_safe=False,
      entry_points="""
      [console_scripts]
      whatsupgit = whatsupgit.main:main
      """
     )