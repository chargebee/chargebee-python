import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Item(Model):
    class ApplicableItem(Model):
      fields = ["id"]
      pass
    class BundleItem(Model):
      fields = ["item_id", "item_type", "quantity", "price_allocation"]
      pass
    class BundleConfiguration(Model):
      fields = ["type"]
      pass

    fields = ["id", "name", "external_name", "description", "status", "resource_version", "updated_at", \
    "item_family_id", "type", "is_shippable", "is_giftable", "redirect_url", "enabled_for_checkout", \
    "enabled_in_portal", "included_in_mrr", "item_applicability", "gift_claim_redirect_url", "unit", \
    "metered", "usage_calculation", "is_percentage_pricing", "archived_at", "channel", "applicable_items", \
    "bundle_items", "bundle_configuration", "metadata", "deleted", "business_entity_id"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
            "metadata": 0,
        }
        return request.send('post', request.uri_path("items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("items",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        json_keys = { 
            "metadata": 0,
        }
        return request.send('post', request.uri_path("items",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("items",id,"delete"), None, env, headers, None, False,json_keys)
