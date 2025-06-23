import json
import unittest
from unittest.mock import patch, Mock

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


class MockEnvironment:
    def __init__(self):
        self.api_key = "test_key"
        self.connect_timeout = 2
        self.read_timeout = 5
        self.enable_debug_logs = False

    def api_url(self, path, subdomain=None):
        return "https://mock.chargebee.com" + path

    def get_retry_config(self):
        return MockRetryConfig()


class RequestTests(unittest.TestCase):

    @patch("requests.request")
    def test_successful_request(self, mock_request):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({"message": "success"})
        mock_response.headers = {}
        mock_request.return_value = mock_response

        from chargebee.http_request import request

        resp, headers, status = request("GET", "/test", MockEnvironment(), params={})

        self.assertEqual(status, 200)
        self.assertEqual(resp["message"], "success")

    @patch("requests.request")
    def test_rate_limit_retry(self, mock_request):
        retry_response = Mock()
        retry_response.status_code = 429
        retry_response.text = json.dumps({"api_error_code": "rate_limit"})
        retry_response.headers = {"Retry-After": "1"}

        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({"message": "ok"})
        success_response.headers = {}

        mock_request.side_effect = [retry_response, success_response]

        from chargebee.http_request import request

        resp, headers, status = request("GET", "/test", MockEnvironment(), params={})

        self.assertEqual(status, 200)
        self.assertEqual(resp["message"], "ok")
        self.assertEqual(mock_request.call_count, 2)

    @patch("requests.request")
    def test_retry_until_max_retries(self, mock_request):
        error_response = Mock()
        error_response.status_code = 503
        error_response.text = "503 Service Unavailable"
        error_response.headers = {}

        mock_request.return_value = error_response

        from chargebee.http_request import request

        with self.assertRaises(Exception) as context:
            request("GET", "/test", MockEnvironment(), params={})

        err = context.exception
        self.assertIsInstance(err, Exception)
        self.assertIn("internal_temporary_error", str(err))
        self.assertEqual(mock_request.call_count, 4)  # 1 original + 3 retries

    @patch("requests.request")
    def test_no_retry_on_400(self, mock_request):
        error_json = {"api_error_code": "invalid_request", "type": "invalid_request"}
        error_response = Mock()
        error_response.status_code = 400
        error_response.text = json.dumps(error_json)
        error_response.headers = {}

        mock_request.return_value = error_response

        from chargebee.http_request import request

        with self.assertRaises(InvalidRequestError) as context:
            request("POST", "/test", MockEnvironment(), params={"x": "y"})

        err = context.exception
        self.assertEqual(err.http_code, 400)
        self.assertEqual(err.api_error_code, "invalid_request")
        self.assertEqual(mock_request.call_count, 1)

    @patch("requests.request")
    def test_custom_retry_on_header_parsing(self, mock_request):
        retry_response = Mock()
        retry_response.status_code = 429
        retry_response.text = json.dumps({"api_error_code": "rate_limit"})
        retry_response.headers = {"Retry-After": "2"}

        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({"message": "done"})
        success_response.headers = {}

        mock_request.side_effect = [retry_response, success_response]

        from chargebee.http_request import request

        resp, headers, status = request("GET", "/test", MockEnvironment(), params={})

        self.assertEqual(resp["message"], "done")
        self.assertEqual(mock_request.call_count, 2)


if __name__ == "__main__":
    unittest.main()
