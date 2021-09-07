#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


setup(
    author="Adam Melancon",
    author_email='adammelancon@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Package to generate random Cajun first and last names.",

    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cajun_name_generator',
    name='cajun_name_generator',
    packages=find_packages(include=['cajun_name_generator', 'cajun_name_generator.*']),
    url='https://github.com/adammelancon/cajun_name_generator',
    version='0.1.1',
    zip_safe=False,
)
