# Chargebee Python Client Library - API V2

[![PyPI](https://img.shields.io/pypi/v/chargebee.svg?maxAge=2592000)](https://pypi.python.org/pypi/chargebee)
[![PyPI](https://img.shields.io/pypi/dm/chargebee.svg?maxAge=2592000)](https://pypi.python.org/pypi/chargebee)

This is the Python Library for integrating with Chargebee. Sign up for a Chargebee account [here](https://www.chargebee.com).

Chargebee now supports two API versions - [V1](https://apidocs.chargebee.com/docs/api/v1) and [V2](https://apidocs.chargebee.com/docs/api), of which V2 is the latest release and all future developments will happen in V2. This library is for <b>API version V2</b>. If you’re looking for V1, head to [chargebee-v1 branch](https://github.com/chargebee/chargebee-python/tree/chargebee-v1).

## Installation

Install the latest version 2.x.x of the library with the following commands:

    $ pip install 'chargebee>=2,<3'
  
or
  
    $ easy_install --upgrade 'chargebee>=2,<3'



If you would prefer to install it from source, just checkout the latest version for 2.x.x by ```git checkout [latest 2.x.x release tag]``` and install with the following command:
  
    $ python setup.py install
  
## Documentation

See our [Python API Reference](https://apidocs.chargebee.com/docs/api?lang=python "API Reference").

## Usage

To create a new subscription:
  
    import chargebee
    chargebee.configure(api_key, site)

    res = chargebee.Subscription.create({
    "plan_id" : "basic"
    })

    print res.subscription

## License

See the LICENSE file.
