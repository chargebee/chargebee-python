# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = []
try:
    import json
except ImportError:
    try:
        import simplejson
    except ImportError:
        requires.append('simplejson')  # For Python==2.5

setup(
    name='chargebee',
    version='1.0.3',
    author='ChargeBee',
    author_email='support@chargebee.com',
    url='https://apidocs.chargebee.com/docs/api?lang=python',
    description='Subscription Billing API',
    packages=find_packages(),
    package_data={'chargebee': ['ssl/*.crt']},
    install_requires=requires,
    test_suite='tests',
)
