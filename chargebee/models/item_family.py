import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ItemFamily(Model):

    fields = ["id", "name", "description", "status", "resource_version", "updated_at", "channel", \
    "business_entity_id", "deleted"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("item_families"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("item_families",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("item_families"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("item_families",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("item_families",id,"delete"), None, env, headers, None, False,json_keys)
