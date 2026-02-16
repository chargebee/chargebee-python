import unittest
from enum import Enum

from chargebee import util


class UtilTest(unittest.TestCase):
    def test_serialize(self):
        before = {
            "id": "sub_KyVq7DNSNM7CSD",
            "plan_id": "free",
            "addons": (
                {
                    "id": "monitor",
                    "quantity": 2,
                },
                {
                    "id": "ssl",
                },
            ),
            "card": {
                "first_name": "Rajaraman",
                "last_name": "Santhanam",
                "number": "4111111111111111",
                "expiry_month": "1",
                "expiry_year": "2024",
                "cvv": "007",
            },
        }

        after = {
            "id": "sub_KyVq7DNSNM7CSD",
            "plan_id": "free",
            "addons[id][0]": "monitor",
            "addons[quantity][0]": 2,
            "addons[id][1]": "ssl",
            "card[first_name]": "Rajaraman",
            "card[last_name]": "Santhanam",
            "card[number]": "4111111111111111",
            "card[expiry_month]": "1",
            "card[expiry_year]": "2024",
            "card[cvv]": "007",
        }

        self.assertEqual(after, util.serialize(before))

    def test_convert_to_serializable_with_enum(self):
        """Test that enums are converted to their values"""
        class Status(Enum):
            ACTIVE = "active"
            INACTIVE = "inactive"

        result = util.convert_to_serializable(Status.ACTIVE)
        self.assertEqual(result, "active")

    def test_convert_to_serializable_with_dict_containing_enum(self):
        """Test that enums in dicts are converted to their values"""
        class Status(Enum):
            ACTIVE = "active"
            INACTIVE = "inactive"

        input_dict = {
            "name": "test",
            "status": Status.ACTIVE,
            "count": 42,
        }

        result = util.convert_to_serializable(input_dict)
        expected = {
            "name": "test",
            "status": "active",
            "count": 42,
        }
        self.assertEqual(result, expected)

    def test_convert_to_serializable_with_nested_dict(self):
        """Test that nested dicts with enums are handled correctly"""
        class Status(Enum):
            ACTIVE = "active"

        class Type(Enum):
            PREMIUM = "premium"

        input_dict = {
            "user": {
                "name": "John",
                "status": Status.ACTIVE,
                "subscription": {
                    "type": Type.PREMIUM,
                    "active": True,
                },
            },
            "count": 10,
        }

        result = util.convert_to_serializable(input_dict)
        expected = {
            "user": {
                "name": "John",
                "status": "active",
                "subscription": {
                    "type": "premium",
                    "active": True,
                },
            },
            "count": 10,
        }
        self.assertEqual(result, expected)

    def test_convert_to_serializable_with_list(self):
        """Test that lists with enums are converted correctly"""
        class Status(Enum):
            ACTIVE = "active"
            INACTIVE = "inactive"

        input_list = [Status.ACTIVE, "test", 42, Status.INACTIVE]
        result = util.convert_to_serializable(input_list)
        expected = ["active", "test", 42, "inactive"]
        self.assertEqual(result, expected)

    def test_convert_to_serializable_with_tuple(self):
        """Test that tuples with enums are converted correctly and remain tuples"""
        class Status(Enum):
            ACTIVE = "active"
            INACTIVE = "inactive"

        input_tuple = (Status.ACTIVE, "test", 42, Status.INACTIVE)
        result = util.convert_to_serializable(input_tuple)
        expected = ("active", "test", 42, "inactive")
        self.assertEqual(result, expected)
        self.assertIsInstance(result, tuple)

    def test_convert_to_serializable_with_list_of_dicts(self):
        """Test that lists of dicts with enums are converted correctly"""
        class Status(Enum):
            ACTIVE = "active"
            INACTIVE = "inactive"

        input_list = [
            {"name": "user1", "status": Status.ACTIVE},
            {"name": "user2", "status": Status.INACTIVE},
        ]

        result = util.convert_to_serializable(input_list)
        expected = [
            {"name": "user1", "status": "active"},
            {"name": "user2", "status": "inactive"},
        ]
        self.assertEqual(result, expected)

    def test_convert_to_serializable_with_complex_nested_structure(self):
        """Test complex nested structure with enums at various levels"""
        class Status(Enum):
            ACTIVE = "active"

        class Type(Enum):
            BASIC = "basic"
            PREMIUM = "premium"

        input_data = {
            "users": [
                {
                    "name": "John",
                    "status": Status.ACTIVE,
                    "subscriptions": [
                        {"type": Type.PREMIUM, "price": 99.99},
                        {"type": Type.BASIC, "price": 9.99},
                    ],
                },
            ],
            "metadata": {
                "default_status": Status.ACTIVE,
                "types": (Type.BASIC, Type.PREMIUM),
            },
        }

        result = util.convert_to_serializable(input_data)
        expected = {
            "users": [
                {
                    "name": "John",
                    "status": "active",
                    "subscriptions": [
                        {"type": "premium", "price": 99.99},
                        {"type": "basic", "price": 9.99},
                    ],
                },
            ],
            "metadata": {
                "default_status": "active",
                "types": ("basic", "premium"),
            },
        }
        self.assertEqual(result, expected)

    def test_convert_to_serializable_with_primitive_types(self):
        """Test that primitive types are passed through unchanged"""
        test_cases = [
            ("string", "string"),
            (42, 42),
            (3.14, 3.14),
            (True, True),
            (False, False),
            (None, None),
        ]

        for input_val, expected_val in test_cases:
            result = util.convert_to_serializable(input_val)
            self.assertEqual(result, expected_val)

    def test_convert_to_serializable_with_empty_structures(self):
        """Test that empty dicts, lists, and tuples are handled correctly"""
        self.assertEqual(util.convert_to_serializable({}), {})
        self.assertEqual(util.convert_to_serializable([]), [])
        self.assertEqual(util.convert_to_serializable(()), ())

    def test_convert_to_serializable_with_integer_enum(self):
        """Test that enums with integer values are converted correctly"""
        class Priority(Enum):
            LOW = 1
            MEDIUM = 2
            HIGH = 3

        input_dict = {
            "task": "Test task",
            "priority": Priority.HIGH,
        }

        result = util.convert_to_serializable(input_dict)
        expected = {
            "task": "Test task",
            "priority": 3,
        }
        self.assertEqual(result, expected)
