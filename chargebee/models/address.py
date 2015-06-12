import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Address(Model):

    fields = ["label", "first_name", "last_name", "email", "company", "phone", "addr", "extended_addr", \
    "extended_addr2", "city", "state_code", "state", "country", "zip", "subscription_id"]


    @staticmethod
    def retrieve(params, env=None, headers=None):
        return request.send('get', request.uri_path("addresses"), params, env, headers)

    @staticmethod
    def update(params, env=None, headers=None):
        return request.send('post', request.uri_path("addresses"), params, env, headers)
