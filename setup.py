#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import setup, find_packages
from pip.req import parse_requirements
import pip


install_reqs = reqs = [str(ir.req) for ir in parse_requirements('requirements.txt',
    session=pip.download.PipSession())]
dev_reqs = [str(ir.req) for ir in parse_requirements('requirements_dev.txt',
    session=pip.download.PipSession())]

setup(
    name='marauding_kanchil',
    version='0.1.0',
    description="Tools for destroying data in order to make life easier.",
    long_description="TODO: Fill in",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/marauding_kanchil',
    packages=find_packages(),
    package_dir={'marauding_kanchil':
                 'marauding_kanchil'},
    entry_points={
        'console_scripts': [
            'marauding_kanchil=marauding_kanchil.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='marauding_kanchil',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=dev_reqs
)
