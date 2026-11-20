import asyncio
import datetime
import unittest
from unittest.mock import AsyncMock, Mock, patch

from chargebee.api_error import APIError
from chargebee.http_request import (
    _process_response,
    MAX_RETRY_AFTER_MS,
    _process_response_async,
    parse_retry_after,
)
from chargebee.retry_config import RetryConfig


class RateLimitRetryTests(unittest.TestCase):
    def test_rate_limit_respects_retry_limit(self):
        for asynchronous in (False, True):
            for retries in (0, 2):
                with self.subTest(asynchronous=asynchronous, retries=retries):
                    error = APIError(429, {"message": "limited"}, {"Retry-After": "2"})
                    # A final successful response bounds the regression on broken code.
                    effects = [error] * (retries + 1) + [({}, {}, 200)]
                    request = (
                        AsyncMock(side_effect=effects)
                        if asynchronous
                        else Mock(side_effect=effects)
                    )
                    sleep = AsyncMock() if asynchronous else Mock()
                    suffix = "_async" if asynchronous else ""
                    with (
                        patch("chargebee.http_request._make_request" + suffix, request),
                        patch("chargebee.http_request.sleep" + suffix, sleep),
                    ):
                        with self.assertRaises(APIError) as caught:
                            args = (
                                "https://example.com",
                                {"method": "GET", "headers": {}},
                                RetryConfig(enabled=True, max_retries=retries),
                                False,
                            )
                            if asynchronous:
                                asyncio.run(_process_response_async(*args))
                            else:
                                _process_response(*args)
                        self.assertIs(caught.exception, error)
                        self.assertEqual(request.call_count, retries + 1)
                        self.assertEqual(sleep.call_count, retries)
                        for call in sleep.call_args_list:
                            self.assertEqual(call.args, (2000,))

    def test_retry_after_from_api_error_headers(self):
        for value, expected in (
            ("2", 2000),
            ("0", 0),
            ("-5", 0),
            ("invalid", None),
            ("60", MAX_RETRY_AFTER_MS),
            ("61", None),
            ("86400", None),
        ):
            with self.subTest(value=value):
                error = APIError(429, {}, {"Retry-After": value})
                self.assertEqual(parse_retry_after(error), expected)

    def test_retry_after_http_date(self):
        error = APIError(429, {}, {"Retry-After": "Thu, 01 Oct 2026 12:00:02 GMT"})
        now = datetime.datetime(2026, 10, 1, 12, tzinfo=datetime.timezone.utc)

        class FrozenDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return now

        with patch("chargebee.http_request.datetime.datetime", FrozenDatetime):
            self.assertEqual(parse_retry_after(error), 2000)

    def test_retry_after_http_date_too_far_uses_default_delay(self):
        error = APIError(429, {}, {"Retry-After": "Fri, 01 Oct 2027 12:00:00 GMT"})
        now = datetime.datetime(2026, 10, 1, 12, tzinfo=datetime.timezone.utc)

        class FrozenDatetime(datetime.datetime):
            @classmethod
            def now(cls, tz=None):
                return now

        with patch("chargebee.http_request.datetime.datetime", FrozenDatetime):
            self.assertIsNone(parse_retry_after(error))
