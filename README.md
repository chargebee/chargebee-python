# Chargebee Python Client Library - API V2


This is the Python Library for integrating with Chargebee. Sign up for a Chargebee account [here](https://www.chargebee.com).

## Requirements

Python 3.11 or higher.

## Installation

Install the latest version 3.x.x of the library with the following command:

  
    $ python setup.py install
  
## Documentation

See our [Python API Reference](https://apidocs.chargebee.com/docs/api?lang=python "API Reference").

## Usage

### To create a new subscription:

```python  
import chargebee
from chargebee import Subscription
chargebee.configure(api_key, site)
response = chargebee.Subscription.create(Subscription.CreateParams(
        plan_id= "basic"
    ))
print(response.subscription)
```

### Create an idempotent request:

[Idempotency keys](https://apidocs.chargebee.com/docs/api/idempotency?prod_cat_ver=2) are passed along with request headers to allow a safe retry of POST requests. 

```python
import chargebee
from chargebee.models import customer
from chargebee import Customer
chargebee.configure(api_key, site)
response = Customer.create(Customer.CreateParams(
        first_name="John",
        last_name="Doe",
        email="john@test.com",
        locale="fr-CA",
        billing_address=customer.BillingAddress(
            first_name="John",
            last_name=" Doe",
            line1="PO Box 9999",
            city="Walnut",
            state="California",
            zip="91789",
            country="US"
        )
    ),
        None,
        {"chargebee-idempotency-key": "<<UUID>>"}  # Replace <<UUID>> with a unique string
    )
customer = response.customer
card = response.card
responseHeaders = response.response_headers  # Retrieves response headers
print(responseHeaders)
idempotencyReplayedValue = response.response_headers["chargebee-idempotency-key"]  # Retrieves Idempotency replayed header value
print(idempotencyReplayedValue)
```

## License

See the [LICENSE](./LICENSE) file.
