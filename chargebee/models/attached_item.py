import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class AttachedItem(Model):

    fields = ["id", "parent_item_id", "item_id", "type", "status", "quantity", "quantity_in_decimal", \
    "billing_cycles", "charge_on_event", "charge_once", "created_at", "resource_version", "updated_at", \
    "channel", "business_entity_id", "deleted"]


    @staticmethod
    def create(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("items",id,"attached_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("attached_items",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("attached_items",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("attached_items",id,"delete"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("items",id,"attached_items"), params, env, headers, None, False,json_keys)
