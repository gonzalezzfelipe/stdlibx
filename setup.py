try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="stdlibx",
    requires=['pyyaml'],
    packages=['stdlibx'],
    version='0.0.0',
    test_suite='tests')
