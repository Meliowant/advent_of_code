import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Solutions for Advent of Code",
    version = "0.8.1",
    description = "Python solutions for the Advent of Code event",
    author = "Andrii Borovyi",
    author_email = "andrii.borovyi@gmail.com",
    url="https://github.com/Meliowant/advent_of_code",
    packages=['advent_of_code'],
    long_description=read('README.md'),
    install_requires=['pytest', 'black', 'flake8', 'pylint', 'coverage']
)
