# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'chargebee'))
import version

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
    version=version.VERSION,
    author='ChargeBee',
    author_email='support@chargebee.com',
    url='https://apidocs.chargebee.com/docs/api?lang=python',
    description='Python wrapper for the ChargeBee Subscription Billing API',
    packages=find_packages(),
    package_data={'chargebee': ['ssl/*.crt']},
    install_requires=requires,
    test_suite='tests',
)
