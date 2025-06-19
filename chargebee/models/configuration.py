import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Configuration(Model):

    fields = ["domain", "product_catalog_version", "chargebee_response_schema_type"]


    @staticmethod
    def list(env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("configurations"), None, env, headers, None, False,json_keys)
