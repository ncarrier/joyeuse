#!/usr/bin/env python3
# This file is part of Joyeuse.

# Joyeuse is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Joyeuse is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Joyeuse. If not, see <https://www.gnu.org/licenses/>.

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
        'pillow',
        'tk',
        'pygobject',
    ],
    packages=[
        'joyeuse',
        'joyeuse.cube',
        'joyeuse.misc',
        'joyeuse.settings',
        'joyeuse.ui',
        'joyeuse.i18n'
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
    package_data={
        '': ['./i18n/locales/*/LC_MESSAGES/*.mo']
    },
    entry_points={
        'console_scripts': [
            'joyeuse=joyeuse.__main__:main'
        ]
    }
)
