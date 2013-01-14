from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='oopen',
      version=version,
      description="Object-Oriented File and Path manipulation",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='file path oo',
      author='Andrew Hekman',
      author_email='ajhekman@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
