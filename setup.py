# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='chargebee',
    version='1.0.0',
    author='ChargeBee',
    author_email='support@chargebee.com',
    url='https://apidocs.chargebee.com/docs/api?lang=python',
    description='Subscription billing API',
    packages=find_packages(),
    test_suite='tests',
)