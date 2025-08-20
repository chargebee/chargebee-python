# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "chargebee"))
if sys.version_info < (3, 11):
    sys.exit("Sorry, Python < 3.11 is not supported")
import version

with open("README.md", "r") as file:
    description = file.read()

requires = ["httpx"]

setup(
    name="chargebee",
    version=version.VERSION,
    author="Chargebee",
    author_email="dx@chargebee.com",
    url="https://apidocs.chargebee.com/docs/api?lang=python",
    description="Python wrapper for the Chargebee Subscription Billing API",
    packages=find_packages(exclude=["tests"]),
    package_data={"chargebee": ["ssl/*.crt"]},
    python_requires=">=3.11",
    install_requires=requires,
    test_suite="tests",
    long_description=description,
    long_description_content_type="text/markdown",
)
