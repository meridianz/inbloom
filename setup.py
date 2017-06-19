from setuptools import setup
from setuptools.extension import Extension
from os import path
import sys

pwd = lambda f: path.join(path.abspath(path.dirname(__file__)), f)
contents = lambda f: open(pwd(f)).read().strip()

kwargs = {}
if sys.platform == 'win32':
    kwargs['libraries'] = ['ws2_32']
module = Extension('pyblossom',
    ['pyblossom/pyblossom.c', 'libblossom/bloom.c', 'libblossom/murmur2/MurmurHash2.c'],
    include_dirs=['libblossom/murmur2'],
    **kwargs
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
