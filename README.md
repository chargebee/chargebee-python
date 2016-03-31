# Chargebee Python Client Library - API V1

The python library for integrating with Chargebee Recurring Billing and Subscription Management solution.

Chargebee now supports two API versions - [V1](https://apidocs.chargebee.com/docs/api/v1) and [V2](https://apidocs.chargebee.com/docs/api). This library is for our <b>older API version V1</b>. The library for V2 can be found in the [master branch](https://github.com/chargebee/chargebee-python). 

You'd want to upgrade to V2 to benefit from the new functionality. Click here for the [API V2 Upgradation Guide](https://apidocs.chargebee.com/docs/api/v1#api-v2-upgradation-guide).


## Installation

Install the latest version 1.x.x of the library with the following commands:

    $ pip install 'chargebee<2'
  
or
  
    $ easy_install --upgrade 'chargebee<2'



If you would prefer to install it from source, just checkout the latest version for 1.x.x by ```git checkout [latest 1.x.x release tag]``` and install with the following command:
  
    $ python setup.py install
  
## Documentation

See our [Python API Reference](https://apidocs.chargebee.com/docs/api/v1/?lang=python "API Reference").

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