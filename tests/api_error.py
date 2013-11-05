import unittest

from chargebee.api_error import APIError
from chargebee import http

import sample_data


class ApiErrorTest(unittest.TestCase):

    def test_auth_error(self):
        try:
            chargebee.http.process_response(sample_data.sample_auth_error(), 401)
        except chargebee.APIError as e:
            self.assertEqual(e.message, 'Sorry, authentication failed. Invalid api key')

    def test_param_error(self):
        try:
            chargebee.http.process_response(sample_data.sample_param_error(), 400)
        except chargebee.APIError as e:
            self.assertEqual(e.message, 'param card[gateway] cannot be blank')
