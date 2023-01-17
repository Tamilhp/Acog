#!/usr/bin/env python
"""Installs the libraries and the commands for tamil-web-mining-utils"""

# Usual imports.

from setuptools import setup, find_packages

# We are reading the requirements from the requirements.txt file

long_description = "tamil-web-mining-utils: Utils for the application"

all_requirements = []
with open("requirements.txt") as fr:
    requirements = fr.read().splitlines()
    for req in requirements:
        if len(req.strip()) > 0:
            if not req.startswith("--"):
                all_requirements.append(req)

mypackages = find_packages(exclude=["docs/*", ])

setup(
    name='web_mining_utils',
    version='0.1',
    author="Aganitha Cognitive Solutions Pvt. Ltd.",
    description="Utils for the application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=mypackages,
    install_requires=all_requirements,
    include_package_data=True,
    entry_points='''
        [console_scripts]
    '''
)
