import unittest

from chargebee import util


class UtilTest(unittest.TestCase):

    def test_serialize(self):
        before = {
            'id': 'sub_KyVq7DNSNM7CSD',
            'plan_id': 'free',
            'addons': (
                {
                    'id': 'monitor',
                    'quantity': 2,
                },
                {
                    'id': 'ssl',
                }
            ),
            'card': {
                'first_name': 'Rajaraman',
                'last_name': 'Santhanam',
                'number': '4111111111111111',
                'expiry_month': '1',
                'expiry_year': '2024',
                'cvv': '007',
            }
        }

        after = {
            'id': 'sub_KyVq7DNSNM7CSD',
            'plan_id': 'free',
            'addons[id][0]': 'monitor',
            'addons[quantity][0]': 2,
            'addons[id][1]': 'ssl',
            'card[first_name]': 'Rajaraman',
            'card[last_name]': 'Santhanam',
            'card[number]': '4111111111111111',
            'card[expiry_month]': '1',
            'card[expiry_year]': '2024',
            'card[cvv]': '007',
        }

        self.assertEqual(after, util.serialize(before))
