__author__ = 'samantha'
from setuptools import setup, find_packages
packages = find_packages(exclude=['test'])

setup(name='aiexplore',
      version='0.1',
      description='ai explorations',
      author='Samantha Atkins',
      author_email='sjatkins@protonmoil.com',
      license='internal',
      packages=packages,
      install_requires = ['validators', 'pytube', 'moviepy'],
      zip_safe=False)
