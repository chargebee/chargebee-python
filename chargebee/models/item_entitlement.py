import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ItemEntitlement(Model):

    fields = ["id", "item_id", "item_type", "feature_id", "feature_name", "value", "name"]


    @staticmethod
    def item_entitlements_for_item(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("items",id,"item_entitlements"), params, env, headers, None, False,json_keys)

    @staticmethod
    def item_entitlements_for_feature(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("features",id,"item_entitlements"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_item_entitlements(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("features",id,"item_entitlements"), params, env, headers, None, False,json_keys)

    @staticmethod
    def upsert_or_remove_item_entitlements_for_item(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("items",id,"item_entitlements"), params, env, headers, None, False,json_keys)
