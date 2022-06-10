# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import setup, Command

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(name='tmdbv3api',
      version='1.7.7',
      description='A lightweight Python library for The Movie Database (TMDb) API.',
      long_description=long_descr,
      url='https://github.com/AnthonyBloomer/tmdbv3api',
      author='Anthony Bloomer',
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['tmdbv3api', 'tmdbv3api.objs'],
      keywords=['movie', 'tv' 'movie database', 'tmdb', 'wrapper', 'database', 'themoviedb', 'moviedb', 'api'],
      install_requires=[
          'requests'
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      cmdclass={
          'publish': PublishCommand,
      },
      zip_safe=False)
