from setuptools import setup, Extension
from os import path

pwd = lambda f: path.join(path.abspath(path.dirname(__file__)), f)
contents = lambda f: open(pwd(f)).read().strip()

module = Extension('pyblossom',
    ['pyblossom/pyblossom.c', 'libblossom/bloom.c', 'libblossom/murmur2/MurmurHash2.c'],
    include_dirs=['libblossom/murmur2'],
    libraries = ['ws2_32']
)

setup(
    name='pyblossom',
    author='meridianz',
    author_email="me@meridianz.io",
    description='Bloom filter for python, based on libbloom (fork of inbloom)',
    long_description=contents('README.rst'),
    version=contents('VERSION'),
    url='https://github.com/meridianz/pyblossom',
    ext_modules=[module],
    license='BSD'
)
