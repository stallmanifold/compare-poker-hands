import sys
import setuptools
import os

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # Import here, because imports outside the eggs aren't loaded.
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


config = dict(
    description = 'Compare pairs of poker hands to determine which one wins based on Texas Hold\'em rules.',
    author = 'Stallmanifold',
    url = 'https://github.com/stallmanifold/compare-poker-hands',
    download_url = 'https://github.com/stallmanifold/compare-poker-hands.git',
    author_email = 'stallmanifold@gmail.com',
    version = '0.1',
    install_requires = ['pytest', 'hypothesis'],
    license = "LICENSE-APACHE",
    package_dir = {'': 'src'},
    packages = ['compare_poker_hands'],
    scripts = [],
    name = 'compare-poker-hands',
    tests_require = ['pytest', 'hypothesis'],
    cmdclass = {
        'test': PyTest,
    },
    entry_points = {
        'console_scripts': [ 'compare-poker-hands = compare_poker_hands.compare_poker_hands:main' ]
    }
)

setup(**config)

