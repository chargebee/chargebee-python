import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class BusinessEntity(Model):

    fields = ["id", "name", "status", "deleted", "created_at", "resource_version", "updated_at"]


    @staticmethod
    def create_transfers(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("business_entities","transfers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def get_transfers(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("business_entities","transfers"), params, env, headers, None, False,json_keys)
