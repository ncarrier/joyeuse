#!/usr/bin/env python3
# More info: https://github.com/navdeep-G/setup.py
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'joyeuse', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    install_requires=[
        'tk',
    ],
    packages=[
        'joyeuse',
        'joyeuse.cube',
        'joyeuse.settings',
        'joyeuse.ui'
    ],
    python_requires='>=3.6.0',
    license=about['__license__'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        ('License :: OSI Approved :: GNU General Public License '
         'v3 or later (GPLv3+)'),
        'Topic :: Other/Nonlisted Topic',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [
            'joyeuse=joyeuse.__main__:main'
        ]
    },
    include_package_data=True
)
