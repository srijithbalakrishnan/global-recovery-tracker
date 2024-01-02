#!/usr/bin/env python

"""The setup script."""

import io
from os import path as op
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

here = op.abspath(op.dirname(__file__))

# get the dependencies and installs
with io.open(op.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Srijith Balakrishnan",
    author_email='s.balakrishnan@tudelft.nl',
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="A package to track and map disaster recovery using geospatial datasets and tools",
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='global_recovery_tracker',
    name='global-recovery-tracker',
    packages=find_packages(include=['global_recovery_tracker', 'global_recovery_tracker.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/srijithbalakrishnan/global-recovery-tracker',
    version='0.0.1',
    zip_safe=False,
)
