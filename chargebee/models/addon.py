import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Addon(Model):
    class Tier(Model):
      fields = ["starting_unit", "ending_unit", "price"]
      pass

    fields = ["id", "name", "invoice_name", "description", "pricing_model", "type", "charge_type", \
    "price", "currency_code", "period", "period_unit", "unit", "status", "archived_at", "enabled_in_portal", \
    "tax_code", "avalara_sale_type", "avalara_transaction_type", "avalara_service_type", "sku", \
    "accounting_code", "accounting_category1", "accounting_category2", "is_shippable", "shipping_frequency_period", \
    "shipping_frequency_period_unit", "resource_version", "updated_at", "invoice_notes", "taxable", \
    "tax_profile_id", "meta_data", "tiers"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("addons"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("addons",id), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("addons"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("addons",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("addons",id,"delete"), None, env, headers)

    @staticmethod
    def copy(params, env=None, headers=None):
        return request.send('post', request.uri_path("addons","copy"), params, env, headers)

    @staticmethod
    def unarchive(id, env=None, headers=None):
        return request.send('post', request.uri_path("addons",id,"unarchive"), None, env, headers)
