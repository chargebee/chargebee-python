import asyncio
import json
import unittest
from unittest.mock import patch

from .test_http_request import make_mock_client

customer = {"customer": {"id": "customer-1", "first_name": "John", "last_name": "Doe"}}


class ModelTest(unittest.TestCase):
    @patch("httpx.Client")
    def test_sync_list(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"list": [customer]})
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee import Chargebee, Filters
        from chargebee.models.customer import CustomerResponse

        client = Chargebee(api_key="key", site="test_site")
        response = client.Customer.list(
            client.Customer.ListParams(email=Filters.StringFilter(STARTS_WITH="john"))
        )

        self.assertEqual(response.http_status_code, 200)
        self.assertIsInstance(response.list, list)
        self.assertEqual(len(response.list), 1)
        self.assertIsInstance(response.list[0].customer, CustomerResponse)
        self.assertEqual(response.list[0].customer.id, "customer-1")

    @patch("httpx.AsyncClient")
    def test_async_list(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"list": [customer]}), is_async=True
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__aenter__.return_value = mock_client

        from chargebee import Chargebee, Filters
        from chargebee.models.customer import CustomerResponse

        async def send_request():
            client = Chargebee(api_key="key", site="test_site", use_async_client=True)
            return await client.Customer.list(
                client.Customer.ListParams(
                    email=Filters.StringFilter(STARTS_WITH="john")
                )
            )

        response = asyncio.run(send_request())

        self.assertEqual(response.http_status_code, 200)
        self.assertIsInstance(response.list, list)
        self.assertEqual(len(response.list), 1)
        self.assertIsInstance(response.list[0].customer, CustomerResponse)
        self.assertEqual(response.list[0].customer.id, "customer-1")
