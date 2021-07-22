import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Item(Model):
    class ApplicableItem(Model):
      fields = ["id"]
      pass

    fields = ["id", "name", "description", "status", "resource_version", "updated_at", "item_family_id", \
    "type", "is_shippable", "is_giftable", "redirect_url", "enabled_for_checkout", "enabled_in_portal", \
    "included_in_mrr", "item_applicability", "gift_claim_redirect_url", "unit", "metered", "usage_calculation", \
    "archived_at", "applicable_items", "metadata"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("items"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("items",id), None, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("items",id), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("items"), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("items",id,"delete"), None, env, headers)
