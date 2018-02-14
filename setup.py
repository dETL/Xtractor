import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='xtractor',
    version='0.0.0',
    author='Josh Meek',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    long_description=read('README.md')
)
