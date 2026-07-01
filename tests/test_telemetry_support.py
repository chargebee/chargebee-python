import unittest

from chargebee.telemetry import RequestTelemetryError, TelemetryAttributeKeys
from chargebee.telemetry.telemetry_support import build_request_end_span_attributes


class TelemetrySupportTest(unittest.TestCase):
    def test_uses_chargebee_error_type_for_error_type(self):
        error = RequestTelemetryError(
            message="Not found",
            chargebee_error_code="resource_not_found",
            chargebee_api_error_type="invalid_request",
        )

        attributes = build_request_end_span_attributes(404, error)

        self.assertEqual(
            attributes[TelemetryAttributeKeys.HTTP_RESPONSE_STATUS_CODE], 404
        )
        self.assertEqual(
            attributes[TelemetryAttributeKeys.ERROR_TYPE], "invalid_request"
        )
        self.assertEqual(
            attributes[TelemetryAttributeKeys.CHARGEBEE_ERROR_TYPE], "invalid_request"
        )

    def test_omits_error_type_when_classification_unavailable(self):
        error = RequestTelemetryError(message="request failed")

        attributes = build_request_end_span_attributes(500, error)

        self.assertEqual(
            attributes[TelemetryAttributeKeys.HTTP_RESPONSE_STATUS_CODE], 500
        )
        self.assertNotIn(TelemetryAttributeKeys.ERROR_TYPE, attributes)
        self.assertNotIn(TelemetryAttributeKeys.CHARGEBEE_ERROR_TYPE, attributes)


if __name__ == "__main__":
    unittest.main()
