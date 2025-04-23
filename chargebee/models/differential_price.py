import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class DifferentialPrice(Model):
    class Tier(Model):
      fields = ["starting_unit", "ending_unit", "price", "starting_unit_in_decimal", "ending_unit_in_decimal", "price_in_decimal", "pricing_type", "package_size"]
      pass
    class ParentPeriod(Model):
      fields = ["period_unit", "period"]
      pass

    fields = ["id", "item_price_id", "parent_item_id", "price", "price_in_decimal", "status", \
    "resource_version", "updated_at", "created_at", "modified_at", "tiers", "currency_code", "parent_periods", \
    "business_entity_id", "deleted"]


    @staticmethod
    def create(id, params, env=None, headers=None):
        json_keys = { 
            "period": 1,
        }
        return request.send('post', request.uri_path("item_prices",id,"differential_prices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("differential_prices",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params, env=None, headers=None):
        json_keys = { 
            "period": 1,
        }
        return request.send('post', request.uri_path("differential_prices",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("differential_prices",id,"delete"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("differential_prices"), params, env, headers, None, False,json_keys)
