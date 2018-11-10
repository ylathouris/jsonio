"""Python Package Definition."""

import os
from setuptools import find_packages, setup


root = os.path.dirname(__file__)
src = os.path.relpath(os.path.join(root, 'python'))

setup(
    name='jsonlib',
    version='0.1.0',
    description='JSON Helpers',
    long_description=(
        "The `jsonlib` package provides utility functions for reading "
        "and writing JSON data."
    ),
    long_description_content_type='text/markdown',
    url='https://github.com/ylathouris/jsonlib',
    author='Yani Lathouris',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    keywords='jsonlib, json, utils',
    project_urls={
        #'Documentation': '',
        'Say Thanks!': 'http://saythanks.io/to/ylathouris',
        'Source': 'https://github.com/ylathouris/jsonlib',
        'Tracker': 'https://github.com/ylathouris/jsonlib/issues',
    },
    package_dir={'': src},
    packages=find_packages(src),
    install_requires=[
        'python-dateutil>=2.7.5,<3',
    ],
)
