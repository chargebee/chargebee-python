import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PriceVariant(Model):
    class Attribute(Model):
      fields = ["name", "value"]
      pass

    fields = ["id", "name", "external_name", "variant_group", "description", "status", "created_at", \
    "resource_version", "updated_at", "archived_at", "attributes", "business_entity_id"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("price_variants"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("price_variants",id), None, env, headers)

    @staticmethod
    def update(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("price_variants",id), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("price_variants",id,"delete"), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("price_variants"), params, env, headers)
