import unittest
from unittest.mock import Mock, patch

from chargebee import environment
from chargebee.request import send
from chargebee.telemetry import RequestTelemetryContext, RequestTelemetryResult
from chargebee.telemetry.telemetry_executor import execute_sync


class RecordingAdapter:
    def __init__(self):
        self.events = []
        self.start_context = None
        self.end_result = None

    def on_request_start(self, context, request_headers):
        self.events.append("start")
        self.start_context = context
        request_headers["traceparent"] = "00-test-trace"
        return "span-1"

    def on_request_end(self, handle, result):
        self.events.append("end")
        self.end_result = result


class MockEnvironment(environment.Environment):
    def __init__(self):
        super().__init__({"api_key": "test_key", "site": "acme"})
        self.set_api_endpoint()
        self.use_async_client = False
        self.telemetry_adapter = None


class TelemetryExecutorTest(unittest.TestCase):
    def test_skips_when_no_adapter(self):
        env = MockEnvironment()

        def action(headers):
            return ({}, {}, 200)

        result = execute_sync(
            env, "customer", "list", "get", "/customers", None, None, action
        )
        self.assertEqual(result[2], 200)

    def test_skips_when_no_metadata(self):
        env = MockEnvironment()
        env.telemetry_adapter = RecordingAdapter()

        def action(headers):
            return ({}, {}, 200)

        execute_sync(env, None, None, "get", "/customers", None, None, action)
        self.assertEqual(env.telemetry_adapter.events, [])

    def test_calls_adapter_once_per_api_call(self):
        env = MockEnvironment()
        adapter = RecordingAdapter()
        env.telemetry_adapter = adapter
        attempts = {"count": 0}

        def action(headers):
            attempts["count"] += 1
            if attempts["count"] < 2:
                raise RuntimeError("retry")
            self.assertEqual(headers.get("traceparent"), "00-test-trace")
            return ({}, {}, 200)

        with self.assertRaises(RuntimeError):
            execute_sync(
                env, "customer", "list", "get", "/customers", None, None, action
            )

        execute_sync(env, "customer", "list", "get", "/customers", None, None, action)

        self.assertEqual(adapter.events.count("start"), 2)
        self.assertEqual(adapter.end_result.http_status_code, 200)
        self.assertEqual(adapter.start_context.span_name, "chargebee.customer.list")

    def test_captures_chargebee_request_headers(self):
        env = MockEnvironment()
        adapter = RecordingAdapter()
        env.telemetry_adapter = adapter

        def action(headers):
            return ({}, {}, 200)

        request_headers = {
            "chargebee-foo": "bar",
            "Chargebee-Idempotency-Key": "idem-key-1",
            "Authorization": "Basic super-secret",
            "chargebee-request-origin-ip": "202.170.207.70",
            "chargebee-request-origin-user": "amara@acme.com",
        }

        execute_sync(
            env,
            "customer",
            "list",
            "get",
            "/customers",
            None,
            request_headers,
            action,
        )

        attrs = adapter.start_context.start_attributes
        self.assertEqual(attrs.get("http.request.header.chargebee-foo"), "bar")
        self.assertEqual(
            attrs.get("http.request.header.chargebee-idempotency-key"), "idem-key-1"
        )
        self.assertNotIn("http.request.header.authorization", attrs)
        self.assertNotIn("http.request.header.chargebee-request-origin-ip", attrs)
        self.assertNotIn("http.request.header.chargebee-request-origin-user", attrs)
        self.assertNotIn("202.170.207.70", str(attrs))
        self.assertNotIn("amara@acme.com", str(attrs))

    def test_does_not_mutate_caller_headers(self):
        env = MockEnvironment()
        adapter = RecordingAdapter()
        env.telemetry_adapter = adapter
        original_headers = {"chargebee-foo": "bar"}
        headers = original_headers.copy()
        captured_headers = {}

        def action(request_headers):
            captured_headers.update(request_headers or {})
            return ({}, {}, 200)

        execute_sync(
            env,
            "customer",
            "list",
            "get",
            "/customers",
            None,
            headers,
            action,
        )

        self.assertEqual(captured_headers.get("traceparent"), "00-test-trace")
        self.assertEqual(headers, original_headers)
        self.assertNotIn("traceparent", headers)

    def test_records_chargebee_api_error_attributes(self):
        env = MockEnvironment()
        adapter = RecordingAdapter()
        env.telemetry_adapter = adapter

        from chargebee.api_error import InvalidRequestError

        def action(headers):
            raise InvalidRequestError(
                404,
                {
                    "message": "Not found",
                    "type": "invalid_request",
                    "api_error_code": "resource_not_found",
                    "param": "customer_id",
                },
            )

        with self.assertRaises(InvalidRequestError):
            execute_sync(
                env,
                "customer",
                "retrieve",
                "get",
                "/customers/x",
                None,
                None,
                action,
            )

        end_attrs = adapter.end_result.end_attributes
        self.assertEqual(end_attrs.get("http.response.status_code"), 404)
        self.assertEqual(end_attrs.get("error.type"), "invalid_request")
        self.assertEqual(end_attrs.get("chargebee.error.type"), "invalid_request")

    def test_adapter_failure_does_not_break_request(self):
        env = MockEnvironment()

        class FailingAdapter:
            def on_request_start(self, context, request_headers):
                raise RuntimeError("telemetry failed")

            def on_request_end(self, handle, result):
                pass

        env.telemetry_adapter = FailingAdapter()

        with patch("chargebee.http_request.request") as mock_request:
            mock_request.return_value = ({}, {}, 200)
            send(
                "get",
                "/customers",
                env,
                None,
                None,
                dict,
                None,
                False,
                None,
                None,
                resource="customer",
                operation="list",
            )
            mock_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
