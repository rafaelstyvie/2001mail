# coding:utf-8
from setuptools import setup, find_packages


setup(name='pyia2001xpy',
      version='2.5.0',
      description='ia2001 Cryptographic Tools',
      long_description=open('README.rst').read(),
      classifiers=[],
      keywords='',
      author=' Styvie',
      author_email='rafael_styvie@hotmail.com',
      url='https://github.com/rafaelstyvie',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      tests_require=[
          'nose',
          'mock'
      ],
      install_requires=[
          'cryptography>=0.5.1',
          'expiringdict>=1.1.3',
          'pynacl>=0.2.3',
          'statsd>=3.0.1'
      ],
      )
