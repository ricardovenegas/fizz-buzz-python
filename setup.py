#!/usr/bin/env python

import distutils.core
import pathlib
import pkg_resources
from setuptools import find_packages

with pathlib.Path('README.md').open() as readme_file:
    readme = readme_file.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]
distutils.core.setup(
    author="Ricardo VENEGAS",
    description="Jeu Fizz Buzz en Python",
    install_requires=install_requires,
    long_description=readme,
    long_description_content_type='text/markdown',
    name='fizz-buzz-python',
    packages=find_packages(),
    url='https://github.com/ricardovenegas/fizz-buzz-python.git',
    version='1.0.0'
)
