import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Address(Model):

    fields = ["label", "first_name", "last_name", "email", "company", "phone", "addr", "extended_addr", \
    "extended_addr2", "city", "state_code", "state", "country", "zip", "validation_status", "subscription_id"]


    @staticmethod
    def retrieve(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("addresses"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("addresses"), params, env, headers, None, False,json_keys)
