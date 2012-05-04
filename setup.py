from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.collage.rssdocument',
      version=version,
      description="Add-on that allows displaying RSSDocuments inside a Collage.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='collage plone iservices rss rssdocument',
      author='Noe Nieto',
      author_email='desarrollo@iservices.com.mx',
      url='http://svn.plone.org/svn/collective/collective.collage.rssdocument',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.collage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.Collage',
          'iservices.rssdocument'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
