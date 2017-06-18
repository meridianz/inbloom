from distutils.core import setup, Extension
from os import path

pwd = lambda f: path.join(path.abspath(path.dirname(__file__)), f)
contents = lambda f: open(pwd(f)).read().strip()

module = Extension('inbloom',
    ['inbloom/inbloom.c', 'libblossom/bloom.c', 'libblossom/murmur2/MurmurHash2.c'],
    include_dirs=['libblossom/murmur2'],
    libraries = ['ws2_32']
)

setup(
    name='inbloom',
    author='EverythingMe',
    description='Portable, cross language Bloom Fitler implementation, with compatible libraries in Java and Go',
    long_description=contents('README.rst'),
    version=contents('VERSION'),
    url='https://github.com/EverythingMe/inbloom',
    ext_modules=[module],
    license='BSD',
)
