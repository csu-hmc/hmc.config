from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='hmc.config',
      version=version,
      description="Generic setup for hmc.csuohio.edu",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Jason K. Moore',
      author_email='j.k.moore19@csuohio.edu',
      url='http://hmc.csuohio.edu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hmc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      extras_require={
          'test': ['plone.app.testing']
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      #setup_requires=["PasteScript"],
      #paster_plugins=["ZopeSkel"],
      )
