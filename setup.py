"""Python Package Definition."""

import os
from setuptools import find_packages, setup


root = os.path.dirname(__file__)
src = os.path.relpath(os.path.join(root, 'python'))

setup(
    name='jsonlib',
    version='0.1.0',
    description='JSON IO Utilities',
    package_dir={'': src},
    packages=find_packages(src),
    install_requires=[
        'python-dateutil>=2.7.5,<3',
    ],
)
