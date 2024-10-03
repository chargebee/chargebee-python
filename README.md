# Chargebee Python Client Library v3 (Beta)

This is the Python Library for integrating with Chargebee. Sign up for a Chargebee account [here](https://www.chargebee.com).

## Requirements

Python 3.11 or higher.

## Installation
Install the latest beta version of the library with pip:

```sh
pip install chargebee --pre
```
If you preferred to install it from source, just checkout the latest version for 3.x.x by ```git checkout [latest 3.x.x release tag]``` and install with the following command:

```sh
python setup.py install
```
  
## Documentation

See our [Python API Reference](https://apidocs.chargebee.com/docs/api?lang=python "API Reference").

## Usage

The package needs to be configured with your site's API key, which is available under Configure Chargebee Section. Refer [here](https://www.chargebee.com/docs/2.0/api_keys.html) for more details.
```python
import chargebee
chargebee.configure("api_key", "site")
```

### Configuring Timeouts

```python
import chargebee
chargebee.update_read_timeout_secs(3000)
chargebee.update_connect_timeout_secs(5000)
```

### Creating a new customer:

```python  
import chargebee

response = chargebee.Customer.create(
    chargebee.Customer.CreateParams(
        first_name="John",
        last_name="Doe",
        email="john@test.com",
        locale="fr-CA",
        billing_address=chargebee.Customer.BillingAddress(
            first_name="John",
            last_name=" Doe",
            line1="PO Box 9999",
            city="Walnut",
            state="California",
            zip="91789",
            country="US",
        ),
    )
)
customer = response.customer
card = response.card
```

### Using filters with the List API

For pagination, `offset` is the parameter that is being used. The value used for this parameter must be the value returned in `next_offset` parameter from the previous API call.

```python
import chargebee
from chargebee import Filters

response = chargebee.Customer.list(
    chargebee.Customer.ListParams(
        first_name=Filters.StringFilter(IS="John")
    )
)
offset = response.next_offset
print(offset)
```

### Using enums

There are two variants of enums in chargebee, 
- Global enums - These are defined globally and can be accessed across resources.
- Resource specific enums - These are defined within a resource and can be accessed using the resource class name.

```python
# Global Enum
import chargebee

response = chargebee.Customer.create(
    chargebee.Customer.CreateParams(
        first_name="John",
        auto_collection=chargebee.AutoCollection.ON,  # global enum
    )
)
print(response.customer.cf_host_url)
```
```python
# Resource Specific Enum
import chargebee

response = chargebee.Customer.change_billing_date(
    chargebee.Customer.ChangeBillingDateParams(
        first_name="John",
        billing_day_of_week=chargebee.Customer.BillingDayOfWeek.MONDAY,  # resource specific enum
    )
)
print(response.customer.cf_host_url)
```

### Using custom fields

```python
import chargebee

response = chargebee.Customer.create(
    chargebee.Customer.CreateParams(
        first_name="John",
        cf_host_url="https://john.com",  # `cf_host_url` is a custom field in Customer object
    )
)
print(response.customer.cf_host_url)
```

### Creating an idempotent request:

[Idempotency keys](https://apidocs.chargebee.com/docs/api/idempotency?prod_cat_ver=2) are passed along with request headers to allow a safe retry of POST requests. 

```python
import chargebee

response = chargebee.Customer.create(
    chargebee.Customer.CreateParams(
        first_name="John",
        last_name="Doe",
        email="john@test.com",
        locale="fr-CA",
        billing_address=chargebee.Customer.BillingAddress(
            first_name="John",
            last_name=" Doe",
            line1="PO Box 9999",
            city="Walnut",
            state="California",
            zip="91789",
            country="US",
        ),
    ),
    None,
    {
        "chargebee-idempotency-key": "<<UUID>>"
    },  # Replace <<UUID>> with a unique string
)
customer = response.customer
card = response.card
responseHeaders = response.response_headers  # Retrieves response headers
print(responseHeaders)
idempotencyReplayedValue = response.response_headers["is_idempotency_replayed"]  # Retrieves Idempotency replayed header value
print(idempotencyReplayedValue)
```

### Waiting for Process Completion 

The response from the previous API call must be passed as an argument for `wait_for_export_completion()` or `wait_for_time_travel_completion()`

```python
# Wait For Export Completion
import chargebee
from chargebee import Filters
response = chargebee.Export.customers(
    chargebee.Export.CustomersParams(
        customer=chargebee.Export.CustomersCustomerParams(
            first_name=Filters.StringFilter(IS="198OeJUMpANxQlhO")
        )
    )
)
print(chargebee.Export.wait_for_export_completion(response.export))
```

## Feedback

If you find any bugs or have any feedback, open an issue in this repository or email it to dx@chargebee.com

## License

See the [LICENSE](./LICENSE) file.
