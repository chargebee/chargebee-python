import json
import unittest
import asyncio
from unittest.mock import patch, Mock, AsyncMock

from chargebee import environment
from chargebee.api_error import InvalidRequestError


class MockRetryConfig:
    def __init__(self, retries=3, delay_ms=100, retry_on=None):
        self.retries = retries
        self.delay_ms = delay_ms
        self.retry_on_codes = retry_on or [429, 503]

    def is_enabled(self):
        return True

    def get_max_retries(self):
        return self.retries

    def get_delay_ms(self):
        return self.delay_ms

    def get_retry_on(self):
        return self.retry_on_codes


class MockEnvironment(environment.Environment):
    def __init__(self):
        self.api_key = "test_key"
        self.site = "test_site"
        self.connect_timeout = 2
        self.read_timeout = 5
        self.enable_debug_logs = False
        self.set_api_endpoint()

    def get_retry_config(self):
        return MockRetryConfig()


def make_mock_client(status_code=200, text="", headers={}, is_async=False):
    mock_client = Mock() if not is_async else AsyncMock()
    mock_response = Mock()
    mock_response.status_code = status_code
    mock_response.text = text
    mock_response.headers = headers
    return mock_client, mock_response


class RequestTests(unittest.TestCase):
    @patch("httpx.Client")
    def test_successful_request(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"message": "success"})
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        resp, headers, status = request("GET", "/test", MockEnvironment(), params={})

        self.assertEqual(status, 200)
        self.assertEqual(resp["message"], "success")

    @patch("httpx.Client")
    def test_rate_limit_retry(self, mock_client_class):
        mock_client, retry_response = make_mock_client(
            429, json.dumps({"api_error_code": "rate_limit"}), {"Retry-After": "1"}
        )

        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({"message": "ok"})
        success_response.headers = {}

        mock_client.request.side_effect = [retry_response, success_response]
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        resp, headers, status = request("GET", "/test", MockEnvironment(), params={})

        self.assertEqual(status, 200)
        self.assertEqual(resp["message"], "ok")
        self.assertEqual(mock_client.request.call_count, 2)

    @patch("httpx.Client")
    def test_retry_until_max_retries(self, mock_client_class):
        mock_client, mock_response = make_mock_client(503, "503 Service Unavailable")
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        with self.assertRaises(Exception) as context:
            request("GET", "/test", MockEnvironment(), params={})

        err = context.exception
        self.assertIsInstance(err, Exception)
        self.assertIn("internal_temporary_error", str(err))
        self.assertEqual(mock_client.request.call_count, 4)  # 1 original + 3 retries

    @patch("httpx.Client")
    def test_no_retry_on_400(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            400,
            json.dumps(
                {"api_error_code": "invalid_request", "type": "invalid_request"}
            ),
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        with self.assertRaises(InvalidRequestError) as context:
            request("POST", "/test", MockEnvironment(), params={"x": "y"})

        err = context.exception
        self.assertEqual(err.http_code, 400)
        self.assertEqual(err.api_error_code, "invalid_request")
        self.assertEqual(mock_client.request.call_count, 1)

    @patch("httpx.Client")
    def test_custom_retry_on_header_parsing(self, mock_client_class):
        mock_client, retry_response = make_mock_client(
            429, json.dumps({"api_error_code": "rate_limit"}), {"Retry-After": "2"}
        )

        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({"message": "done"})
        success_response.headers = {}

        mock_client.request.side_effect = [retry_response, success_response]
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        resp, headers, status = request("GET", "/test", MockEnvironment(), params={})

        self.assertEqual(resp["message"], "done")
        self.assertEqual(mock_client.request.call_count, 2)

    @patch("httpx.AsyncClient")
    def test_async_successful_request(self, mock_async_client_class):
        mock_async_client, mock_response = make_mock_client(
            text=json.dumps({"message": "async_success"}), is_async=True
        )
        mock_async_client.request.return_value = mock_response
        mock_async_client_class.return_value.__aenter__.return_value = mock_async_client

        from chargebee.http_request import request

        async def test_async_request():
            resp, headers, status = await request(
                "GET", "/test", MockEnvironment(), params={}, use_async_client=True
            )
            return resp, headers, status

        resp, headers, status = asyncio.run(test_async_request())

        self.assertEqual(status, 200)
        self.assertEqual(resp["message"], "async_success")

    @patch("httpx.AsyncClient")
    def test_async_rate_limit_retry(self, mock_async_client_class):
        mock_async_client, retry_response = make_mock_client(
            429,
            json.dumps({"api_error_code": "rate_limit"}),
            {"Retry-After": "1"},
            is_async=True,
        )

        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({"message": "async_ok"})
        success_response.headers = {}

        mock_async_client.request.side_effect = [retry_response, success_response]
        mock_async_client_class.return_value.__aenter__.return_value = mock_async_client

        from chargebee.http_request import request

        async def test_async_retry():
            resp, headers, status = await request(
                "GET", "/test", MockEnvironment(), params={}, use_async_client=True
            )
            return resp, headers, status

        resp, headers, status = asyncio.run(test_async_retry())

        self.assertEqual(status, 200)
        self.assertEqual(resp["message"], "async_ok")
        self.assertEqual(mock_async_client.request.call_count, 2)

    @patch("httpx.Client")
    def test_json_request_payload(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"message": "json_success"})
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        test_data = {"key": "value", "nested": {"data": "test"}}
        resp, headers, status = request(
            "POST", "/test", MockEnvironment(), params=test_data, isJsonRequest=True
        )

        # Verify that the request was made with json parameter
        call_args = mock_client.request.call_args
        self.assertIn("json", call_args[1])
        self.assertIn("application/json", call_args[1]["headers"]["Content-Type"])
        self.assertEqual(call_args[1]["json"], test_data)
        self.assertNotIn("data", call_args[1])

    @patch("httpx.Client")
    def test_get_request(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"message": "json_success"})
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        params = {"page": 1, "count": 10}
        resp, headers, status = request(
            "GET", "/test", MockEnvironment(), params=params, isJsonRequest=True
        )

        call_args = mock_client.request.call_args
        self.assertNotIn("json", call_args[1])
        self.assertNotIn("data", call_args[1])
        self.assertIn("params", call_args[1])
        self.assertNotIn("Content-Type", call_args[1]["headers"])

    @patch("httpx.Client")
    def test_timeout(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"message": "json_success"})
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        params = {"page": 1, "count": 10}
        env = MockEnvironment()
        resp, headers, status = request(
            "GET", "/test", env, params=params, isJsonRequest=True
        )

        call_args = mock_client.request.call_args
        self.assertEqual(call_args[1]["timeout"].connect, env.connect_timeout)
        self.assertEqual(call_args[1]["timeout"].read, env.read_timeout)

    @patch("httpx.Client")
    def test_subdomain_url(self, mock_client_class):
        mock_client, mock_response = make_mock_client(
            text=json.dumps({"message": "json_success"})
        )
        mock_client.request.return_value = mock_response
        mock_client_class.return_value.__enter__.return_value = mock_client

        from chargebee.http_request import request

        env = MockEnvironment()
        resp, headers, status = request("GET", "/test", env, subDomain="ingest")

        call_args = mock_client.request.call_args
        self.assertEqual(
            call_args[1]["url"], "https://test_site.ingest.chargebee.com/api/v2/test?"
        )
