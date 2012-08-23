from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='geo_file_conv',
      version=version,
      description="Conversion between spatial file formats",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='GIS Shapefie KML',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'pyshp',
          'fastkml',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
