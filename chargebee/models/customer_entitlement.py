import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CustomerEntitlement(Model):

    fields = ["customer_id", "subscription_id", "feature_id", "value", "name", "is_enabled"]


    @staticmethod
    def entitlements_for_customer(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"customer_entitlements"), params, env, headers, None, False,json_keys)
