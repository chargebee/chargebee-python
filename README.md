> [!WARNING]  
> This branch contains the code for Chargebee Python SDK v2 which is deprecated. v2 will continue to receive updates till December 31, 2025. If you are using v2, we request you to upgrade to v3 by following [this migration guide](https://github.com/chargebee/chargebee-python/wiki/Migration-guide-for-v3) before December 31, 2025.

# Chargebee Python Client Library - API V2

[![PyPI](https://img.shields.io/pypi/v/chargebee.svg?maxAge=2)](https://pypi.python.org/pypi/chargebee)
[![PyPI](https://img.shields.io/pypi/dm/chargebee.svg?maxAge=2)](https://pypi.python.org/pypi/chargebee)

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

### To create a new subscription:

```python  
import chargebee
import json
chargebee.configure(api_key, site)
result = chargebee.Subscription.create({
"plan_id" : "basic"
})

print result.subscription
```

### Create an idempotent request:

[Idempotency keys](https://apidocs.chargebee.com/docs/api/idempotency?prod_cat_ver=2) are passed along with request headers to allow a safe retry of POST requests. 

```python
import chargebee
import json
chargebee.configure(api_key, site)
result = chargebee.Customer.create({
    "first_name" : "John",
    "last_name" : "Doe",
    "email" : "john@test.com",
    "locale" : "fr-CA",
    "billing_address" : {
        "first_name" : "John",
        "last_name" : "Doe",
        "line1" : "PO Box 9999",
        "city" : "Walnut",
        "state" : "California",
        "zip" : "91789",
        "country" : "US"
        }
    },
    None,
    {"chargebee-idempotency-key" : "<<UUID>>"}  # Replace <<UUID>> with a unique string
    )
customer = result.customer
card = result.card
responseHeaders = result.get_response_headers # Retrieves response headers
print(responseHeaders) 
idempotencyReplayedValue = result.is_idempotency_replayed # Retrieves Idempotency replayed header value
print(idempotencyReplayedValue) 
```
`isIdempotencyReplayed()` method can be accessed to differentiate between original and replayed requests.

## License

See the LICENSE file.
