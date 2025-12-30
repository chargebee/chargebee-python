import unittest
from dataclasses import dataclass
from typing import List, Dict, Any
from chargebee.responses import Response
from chargebee.response import Response as ResponseBase
from chargebee.model import Model
from dataclasses import is_dataclass


# Test fixtures - Response models
@dataclass
class AddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    line1: str = None
    line2: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None


@dataclass
class PhoneResponse(Model):
    raw_data: Dict[Any, Any] = None
    number: str = None
    type: str = None


@dataclass
class CustomerResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    created_at: int = None
    updated_at: int = None
    active: bool = None
    billing_address: AddressResponse = None
    phone_numbers: List[PhoneResponse] = None
    meta_data: Any = None


@dataclass
class ListOfObjects(ResponseBase):
    customer: List[CustomerResponse]


@dataclass
class CreateCustomerResponse(ResponseBase):
    is_idempotency_replayed: bool
    customer: CustomerResponse


@dataclass
class ListCustomerItem:
    customer: CustomerResponse


@dataclass
class ListCustomerResponse(ResponseBase):
    list: List[ListCustomerItem]
    next_offset: str = None


class TestResponseParsing(unittest.TestCase):
    """Test cases for Response.parse_response() - single response parsing"""

    def test_parse_response_with_primitives(self):
        """Test parsing a response with primitive types"""
        response_data = {
            "customer": {
                "id": "cust_123",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "+1234567890",
                "created_at": 1609459200,
                "updated_at": 1609545600,
                "active": True,
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_123")
        self.assertEqual(parsed.customer.first_name, "John")
        self.assertEqual(parsed.customer.last_name, "Doe")
        self.assertEqual(parsed.customer.email, "john@example.com")
        self.assertEqual(parsed.customer.phone, "+1234567890")
        self.assertEqual(parsed.customer.created_at, 1609459200)
        self.assertEqual(parsed.customer.updated_at, 1609545600)
        self.assertEqual(parsed.customer.active, True)
        self.assertEqual(parsed.headers, response_headers)
        self.assertEqual(parsed.http_status_code, http_code)

    def test_parse_response_with_nested_object(self):
        """Test parsing a response with nested objects"""
        response_data = {
            "customer": {
                "id": "cust_456",
                "first_name": "Jane",
                "last_name": "Smith",
                "email": "jane@example.com",
                "billing_address": {
                    "line1": "123 Main St",
                    "line2": "Apt 4B",
                    "city": "New York",
                    "state": "NY",
                    "zip": "10001",
                    "country": "US",
                },
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_456")
        self.assertEqual(parsed.customer.first_name, "Jane")
        self.assertIsNotNone(parsed.customer.billing_address)
        self.assertIsInstance(parsed.customer.billing_address, AddressResponse)
        self.assertEqual(parsed.customer.billing_address.line1, "123 Main St")
        self.assertEqual(parsed.customer.billing_address.line2, "Apt 4B")
        self.assertEqual(parsed.customer.billing_address.city, "New York")
        self.assertEqual(parsed.customer.billing_address.state, "NY")
        self.assertEqual(parsed.customer.billing_address.zip, "10001")
        self.assertEqual(parsed.customer.billing_address.country, "US")

    def test_parse_response_with_list_of_objects(self):
        """Test parsing a response with a list of nested objects"""
        response_data = {
            "customer": {
                "id": "cust_789",
                "first_name": "Bob",
                "last_name": "Johnson",
                "email": "bob@example.com",
                "phone_numbers": [
                    {"number": "+1234567890", "type": "home"},
                    {"number": "+0987654321", "type": "work"},
                ],
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_789")
        self.assertIsNotNone(parsed.customer.phone_numbers)
        self.assertEqual(len(parsed.customer.phone_numbers), 2)
        self.assertIsInstance(parsed.customer.phone_numbers[0], PhoneResponse)
        self.assertEqual(parsed.customer.phone_numbers[0].number, "+1234567890")
        self.assertEqual(parsed.customer.phone_numbers[0].type, "home")
        self.assertIsInstance(parsed.customer.phone_numbers[1], PhoneResponse)
        self.assertEqual(parsed.customer.phone_numbers[1].number, "+0987654321")
        self.assertEqual(parsed.customer.phone_numbers[1].type, "work")

    def test_parse_response_with_any_type_dict(self):
        """Test parsing a response with Any type field containing a dict"""
        response_data = {
            "customer": {
                "id": "cust_999",
                "first_name": "Alice",
                "last_name": "Brown",
                "email": "alice@example.com",
                "meta_data": {"key1": "value1", "key2": "value2", "nested": {"a": 1}},
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_999")
        self.assertIsNotNone(parsed.customer.meta_data)
        self.assertIsInstance(parsed.customer.meta_data, dict)
        self.assertEqual(parsed.customer.meta_data["key1"], "value1")
        self.assertEqual(parsed.customer.meta_data["key2"], "value2")
        self.assertIn("nested", parsed.customer.meta_data)
        self.assertEqual(parsed.customer.meta_data["nested"]["a"], 1)

    def test_parse_response_with_any_type_list(self):
        """Test parsing a response with Any type field containing a list"""
        response_data = {
            "customer": {
                "id": "cust_888",
                "first_name": "Charlie",
                "last_name": "Davis",
                "email": "charlie@example.com",
                "meta_data": ["tag1", "tag2", "tag3"],
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_888")
        self.assertIsNotNone(parsed.customer.meta_data)
        self.assertIsInstance(parsed.customer.meta_data, list)
        self.assertEqual(len(parsed.customer.meta_data), 3)
        self.assertEqual(parsed.customer.meta_data[0], "tag1")
        self.assertEqual(parsed.customer.meta_data[1], "tag2")
        self.assertEqual(parsed.customer.meta_data[2], "tag3")

    def test_parse_response_with_idempotency_replayed_true(self):
        """Test parsing a response with idempotency replayed header set to true"""
        response_data = {
            "customer": {
                "id": "cust_111",
                "first_name": "David",
                "last_name": "Wilson",
                "email": "david@example.com",
            }
        }
        response_headers = {
            "content-type": "application/json",
            "chargebee-idempotency-replayed": "true",
        }
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertTrue(parsed.is_idempotency_replayed)
        self.assertEqual(parsed.customer.id, "cust_111")

    def test_parse_response_with_idempotency_replayed_false(self):
        """Test parsing a response with idempotency replayed header set to false"""
        response_data = {
            "customer": {
                "id": "cust_222",
                "first_name": "Emma",
                "last_name": "Taylor",
                "email": "emma@example.com",
            }
        }
        response_headers = {
            "content-type": "application/json",
            "chargebee-idempotency-replayed": "",
        }
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertFalse(parsed.is_idempotency_replayed)
        self.assertEqual(parsed.customer.id, "cust_222")

    def test_parse_response_with_missing_optional_fields(self):
        """Test parsing a response with missing optional fields"""
        response_data = {
            "customer": {
                "id": "cust_333",
                "first_name": "Frank",
                "email": "frank@example.com",
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 201

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_333")
        self.assertEqual(parsed.customer.first_name, "Frank")
        self.assertIsNone(parsed.customer.last_name)
        self.assertEqual(parsed.customer.email, "frank@example.com")
        self.assertIsNone(parsed.customer.phone)
        self.assertIsNone(parsed.customer.billing_address)
        self.assertEqual(parsed.http_status_code, 201)


class TestListResponseParsing(unittest.TestCase):
    """Test cases for Response.parse_list_response() - list response parsing"""

    def test_parse_list_response_with_single_item(self):
        """Test parsing a list response with a single item"""
        response_data = {
            "list": [
                {
                    "customer": {
                        "id": "cust_list_1",
                        "first_name": "Grace",
                        "last_name": "Miller",
                        "email": "grace@example.com",
                        "active": True,
                    }
                }
            ]
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_list_response()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertIsNotNone(parsed.list)
        self.assertEqual(len(parsed.list), 1)
        self.assertIsInstance(parsed.list[0], ListCustomerItem)
        self.assertEqual(parsed.list[0].customer.id, "cust_list_1")
        self.assertEqual(parsed.list[0].customer.first_name, "Grace")
        self.assertEqual(parsed.list[0].customer.last_name, "Miller")
        self.assertEqual(parsed.list[0].customer.email, "grace@example.com")
        self.assertEqual(parsed.list[0].customer.active, True)
        self.assertEqual(parsed.headers, response_headers)
        self.assertEqual(parsed.http_status_code, http_code)

    def test_parse_list_response_with_multiple_items(self):
        """Test parsing a list response with multiple items"""
        response_data = {
            "list": [
                {
                    "customer": {
                        "id": "cust_list_2",
                        "first_name": "Henry",
                        "last_name": "Garcia",
                        "email": "henry@example.com",
                        "created_at": 1609459200,
                    }
                },
                {
                    "customer": {
                        "id": "cust_list_3",
                        "first_name": "Ivy",
                        "last_name": "Martinez",
                        "email": "ivy@example.com",
                        "created_at": 1609545600,
                    }
                },
                {
                    "customer": {
                        "id": "cust_list_4",
                        "first_name": "Jack",
                        "last_name": "Anderson",
                        "email": "jack@example.com",
                        "created_at": 1609632000,
                    }
                },
            ]
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_list_response()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertEqual(len(parsed.list), 3)

        self.assertEqual(parsed.list[0].customer.id, "cust_list_2")
        self.assertEqual(parsed.list[0].customer.first_name, "Henry")
        self.assertEqual(parsed.list[0].customer.created_at, 1609459200)

        self.assertEqual(parsed.list[1].customer.id, "cust_list_3")
        self.assertEqual(parsed.list[1].customer.first_name, "Ivy")
        self.assertEqual(parsed.list[1].customer.created_at, 1609545600)

        self.assertEqual(parsed.list[2].customer.id, "cust_list_4")
        self.assertEqual(parsed.list[2].customer.first_name, "Jack")
        self.assertEqual(parsed.list[2].customer.created_at, 1609632000)

    def test_parse_list_response_with_next_offset(self):
        """Test parsing a list response with next_offset for pagination"""
        response_data = {
            "list": [
                {
                    "customer": {
                        "id": "cust_list_5",
                        "first_name": "Kate",
                        "last_name": "Lopez",
                        "email": "kate@example.com",
                    }
                }
            ],
            "next_offset": "offset_abc123",
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_list_response()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertEqual(len(parsed.list), 1)
        self.assertEqual(parsed.list[0].customer.id, "cust_list_5")
        self.assertEqual(parsed.next_offset, "offset_abc123")

    def test_parse_list_response_without_next_offset(self):
        """Test parsing a list response without next_offset (last page)"""
        response_data = {
            "list": [
                {
                    "customer": {
                        "id": "cust_list_6",
                        "first_name": "Leo",
                        "last_name": "Hernandez",
                        "email": "leo@example.com",
                    }
                }
            ]
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_list_response()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertEqual(len(parsed.list), 1)
        self.assertIsNone(parsed.next_offset)

    def test_parse_list_response_with_empty_list(self):
        """Test parsing a list response with an empty list"""
        response_data = {"list": []}
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_list_response()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertEqual(len(parsed.list), 0)
        self.assertIsNone(parsed.next_offset)

    def test_parse_list_response_with_nested_objects(self):
        """Test parsing a list response with nested objects in items"""
        response_data = {
            "list": [
                {
                    "customer": {
                        "id": "cust_list_7",
                        "first_name": "Mia",
                        "last_name": "Clark",
                        "email": "mia@example.com",
                        "billing_address": {
                            "line1": "456 Oak Ave",
                            "city": "Boston",
                            "state": "MA",
                            "zip": "02101",
                            "country": "US",
                        },
                    }
                }
            ]
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_list_response()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertEqual(len(parsed.list), 1)
        self.assertEqual(parsed.list[0].customer.id, "cust_list_7")
        self.assertIsNotNone(parsed.list[0].customer.billing_address)
        self.assertIsInstance(parsed.list[0].customer.billing_address, AddressResponse)
        self.assertEqual(parsed.list[0].customer.billing_address.line1, "456 Oak Ave")
        self.assertEqual(parsed.list[0].customer.billing_address.city, "Boston")


class TestParseMethod(unittest.TestCase):
    """Test cases for Response.parse() - should delegate correctly"""

    def test_parse_delegates_to_parse_response_for_single_response(self):
        """Test that parse() delegates to parse_response() for single responses"""
        response_data = {
            "customer": {
                "id": "cust_parse_1",
                "first_name": "Noah",
                "last_name": "Lee",
                "email": "noah@example.com",
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_parse_1")
        self.assertEqual(parsed.customer.first_name, "Noah")

    def test_parse_delegates_to_parse_list_response_for_list_response(self):
        """Test that parse() delegates to parse_list_response() for list responses"""
        response_data = {
            "list": [
                {
                    "customer": {
                        "id": "cust_parse_2",
                        "first_name": "Olivia",
                        "last_name": "Walker",
                        "email": "olivia@example.com",
                    }
                }
            ]
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            ListCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse()

        self.assertIsInstance(parsed, ListCustomerResponse)
        self.assertEqual(len(parsed.list), 1)
        self.assertEqual(parsed.list[0].customer.id, "cust_parse_2")


class TestResponseUtilityMethods(unittest.TestCase):
    """Test cases for Response utility methods"""

    def test_is_idempotency_replayed_with_header_present(self):
        """Test is_idempotency_replayed() when header is present"""
        response_data = {"customer": {"id": "cust_test"}}
        response_headers = {"chargebee-idempotency-replayed": "true"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )

        self.assertTrue(response.is_idempotency_replayed())

    def test_is_idempotency_replayed_with_header_absent(self):
        """Test is_idempotency_replayed() when header is absent"""
        response_data = {"customer": {"id": "cust_test"}}
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )

        self.assertFalse(response.is_idempotency_replayed())

    def test_http_status_code_returns_correct_code(self):
        """Test http_status_code() returns the correct HTTP status code"""
        response_data = {"customer": {"id": "cust_test"}}
        response_headers = {"content-type": "application/json"}
        http_code = 201

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )

        self.assertEqual(response.http_status_code(), 201)

    def test_http_status_code_converts_to_int(self):
        """Test http_status_code() converts string to int"""
        response_data = {"customer": {"id": "cust_test"}}
        response_headers = {"content-type": "application/json"}
        http_code = "200"

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )

        result = response.http_status_code()
        self.assertEqual(result, 200)
        self.assertIsInstance(result, int)

    def test_parse_response_with_any_type_json(self):
        """Test parsing a response with Any type field containing JSON/dict"""
        response_data = {
            "customer": {
                "id": "cust_999",
                "first_name": "Dana",
                "last_name": "Smith",
                "email": "dana@example.com",
                "meta_data": {
                    "source": "campaign",
                    "tier": "gold",
                    "active": True,
                },
            }
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(
            CreateCustomerResponse, response_data, response_headers, http_code
        )
        parsed = response.parse_response()

        self.assertIsInstance(parsed, CreateCustomerResponse)
        self.assertEqual(parsed.customer.id, "cust_999")

        # meta_data assertions
        self.assertIsNotNone(parsed.customer.meta_data)
        self.assertIsInstance(parsed.customer.meta_data, dict)
        self.assertEqual(parsed.customer.meta_data["source"], "campaign")
        self.assertEqual(parsed.customer.meta_data["tier"], "gold")
        self.assertTrue(parsed.customer.meta_data["active"])

    def test_parse_response_non_list_based_list_response(self):
        """Test parsing a response with Any type field containing JSON/dict"""
        response_data = {
            "customer": [
                {
                    "id": "cust_999",
                    "first_name": "Dana",
                    "last_name": "Smith",
                    "email": "dana@example.com",
                    "meta_data": {
                        "source": "campaign",
                        "tier": "gold",
                        "active": True,
                    },
                },
                {
                    "id": "cust_111",
                    "first_name": "Dana",
                    "last_name": "Smith",
                    "email": "dana@example.com",
                    "meta_data": {
                        "source": "campaign",
                        "tier": "gold",
                        "active": True,
                    },
                },
            ]
        }
        response_headers = {"content-type": "application/json"}
        http_code = 200

        response = Response(ListOfObjects, response_data, response_headers, http_code)
        parsed = response.parse_response()

        self.assertIsInstance(parsed, ListOfObjects)
        self.assertEqual(len(parsed.customer), 2)

        for customer in parsed.customer:
            self.assertTrue(is_dataclass(customer))
            self.assertIsInstance(customer, CustomerResponse)


if __name__ == "__main__":
    unittest.main()
