# Chargebee Python Client Library v3

> [!NOTE]
> [![Join Discord](https://img.shields.io/badge/Discord-Early%20Access-blue?logo=discord&logoColor=white)](https://discord.gg/S3SXDzXHAg)
>
> We are trialing a Discord server for developers building with Chargebee. Limited spots are open on a first-come basis. Join [here](https://discord.gg/S3SXDzXHAg) if interested.


This is the official Python library for integrating with Chargebee.
- 📘 For a complete reference of available APIs, check out our [API Documentation](https://apidocs.chargebee.com/docs/api/?lang=python).  
- 🧪 To explore and test API capabilities interactively, head over to our [API Explorer](https://api-explorer.chargebee.com).

If you're upgrading from an older version please refer to the [Migration Guide](https://github.com/chargebee/chargebee-python/wiki/Migration-guide-for-v3)

## Requirements

- Python 3.11+

## Installation
Install the latest version of the library with pip:

```sh
pip install chargebee
```
Install from source with:

```sh
python setup.py install
```
  
## Documentation

See our [Python API Reference](https://apidocs.chargebee.com/docs/api?lang=python "API Reference").

## Usage

The package needs to be configured with your site's API key, which is available under Configure Chargebee Section. Refer [here](https://www.chargebee.com/docs/2.0/api_keys.html) for more details.

### Configuring chargebee client
```python
from chargebee import Chargebee
cb_client = Chargebee(api_key="", site="")
```

### Configuring Timeouts

```python
from chargebee import Chargebee
cb_client = Chargebee(api_key="api_key", site="site")
cb_client.update_read_timeout_secs(3000)
cb_client.update_connect_timeout_secs(5000)
```

### Configuring Retry Delays

```python
from chargebee import Chargebee
cb_client = Chargebee(api_key="api_key", site="site")
cb_client.update_export_retry_delay_ms(3000)
cb_client.update_time_travel_retry_delay_ms(5000)
```

### Making API Request:

```python  
# Create a Customer

response = cb_client.Customer.create(
    cb_client.Customer.CreateParams(
        first_name="John",
        last_name="Doe",
        email="john@test.com",
        locale="fr-CA",
        billing_address=cb_client.Customer.BillingAddress(
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

### Async HTTP client

Starting with version `3.9.0`, the Chargebee Python SDK can optionally be configured to use an asynchronous HTTP client which uses `asyncio` to perform non-blocking requests. This can be enabled by passing the `use_async_client=True` argument to the constructor:

```python
cb_client = Chargebee(api_key="api_key", site="site", use_async_client=True)
```

When configured to use the async client, all model methods return a coroutine, which will have to be awaited to get the response:

```python
async def get_customers():
    response = await cb_client.Customer.list(
        cb_client.Customer.ListParams(
            first_name=Filters.StringFilter(IS="John")
        )
    )
    return response
```

Note: The async methods will have to be wrapped in an event loop during invocation. For example, the `asyncio.run` method can be used to run the above example:

```python
import asyncio
response = asyncio.run(get_customers())
```

### List API Request With Filter

For pagination, `offset` is the parameter that is being used. The value used for this parameter must be the value returned in `next_offset` parameter from the previous API call.

```python
from chargebee import Filters

response = cb_client.Customer.list(
    cb_client.Customer.ListParams(
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

response = cb_client.Customer.create(
    cb_client.Customer.CreateParams(
        first_name="John",
        auto_collection=chargebee.AutoCollection.ON,  # global enum
    )
)
print(response.customer)
```
```python
# Resource Specific Enum

response = cb_client.Customer.change_billing_date(
    cb_client.Customer.ChangeBillingDateParams(
        first_name="John",
        billing_day_of_week=cb_client.Customer.BillingDayOfWeek.MONDAY,  # resource specific enum
    )
)
print(response.customer)
```

### Using custom fields

```python
response = cb_client.Customer.create(
    cb_client.Customer.CreateParams(
        first_name="John",
        cf_host_url="https://john.com",  # `cf_host_url` is a custom field in Customer object
    )
)
print(response.customer.cf_host_url)
```

### Creating an idempotent request:

[Idempotency keys](https://apidocs.chargebee.com/docs/api/idempotency?prod_cat_ver=2) are passed along with request headers to allow a safe retry of POST requests. 

```python
response = cb_client.Customer.create(
    cb_client.Customer.CreateParams(
        first_name="John",
        last_name="Doe",
        email="john@test.com",
        locale="fr-CA",
        billing_address=cb_client.Customer.BillingAddress(
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
responseHeaders = response.headers  # Retrieves response headers
print(responseHeaders)
idempotencyReplayedValue = response.is_idempotency_replayed  # Retrieves Idempotency replayed header value
print(idempotencyReplayedValue)
```

### Waiting for Process Completion 

The response from the previous API call must be passed as an argument for `wait_for_export_completion()` or `wait_for_time_travel_completion()`

```python
# Wait For Export Completion

from chargebee import Filters

response = cb_client.Export.customers(
    cb_client.Export.CustomersParams(
        customer=cb_client.Export.CustomersCustomerParams(
            first_name=Filters.StringFilter(IS="John")
        )
    )
)
print(cb_client.Export.wait_for_export_completion(response.export))
```

### Retry Handling

Chargebee's SDK includes built-in retry logic to handle temporary network issues and server-side errors. This feature is **disabled by default** but can be **enabled when needed**.

#### Key features include:

- **Automatic retries for specific HTTP status codes**: Retries are automatically triggered for status codes `500`, `502`, `503`, and `504`.
- **Exponential backoff**: Retry delays increase exponentially to prevent overwhelming the server.
- **Rate limit management**: If a `429 Too Many Requests` response is received with a `Retry-After` header, the SDK waits for the specified duration before retrying.
  > *Note: Exponential backoff and max retries do not apply in this case.*
- **Customizable retry behavior**: Retry logic can be configured using the `retryConfig` parameter in the environment configuration.

#### Example: Customizing Retry Logic

You can enable and configure the retry logic by passing a `retryConfig` object when initializing the Chargebee environment:

```python
from chargebee import Chargebee
from chargebee.retry_config import RetryConfig

retry_config = RetryConfig(
    enabled=True,
    max_retries=5,
    delay_ms=1000,
    retry_on=[500]
)
cb_client = Chargebee(api_key="api_key", site="site")
cb_client.update_retry_config(retry_config)

# ... your Chargebee API operations ...

```

#### Example: Rate Limit retry logic

You can enable and configure the retry logic for rate-limit by passing a `retryConfig` object when initializing the Chargebee environment:

```python
from chargebee import Chargebee
from chargebee.retry_config import RetryConfig

retry_config = RetryConfig(
    enabled=True,
    max_retries=5,
    delay_ms=1000,
    retry_on=[429]
)
cb_client = Chargebee(api_key="api_key", site="site")
cb_client.update_retry_config(retry_config)

# ... your Chargebee API operations ...

```


## Feedback

If you find any bugs or have any feedback, open an issue in this repository or email it to dx@chargebee.com

## License

See the [LICENSE](./LICENSE) file.
