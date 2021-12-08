import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ItemPrice(Model):
    class Tier(Model):
      fields = ["starting_unit", "ending_unit", "price", "starting_unit_in_decimal", "ending_unit_in_decimal", "price_in_decimal"]
      pass
    class TaxDetail(Model):
      fields = ["tax_profile_id", "avalara_sale_type", "avalara_transaction_type", "avalara_service_type", "avalara_tax_code", "hsn_code", "taxjar_product_code"]
      pass
    class AccountingDetail(Model):
      fields = ["sku", "accounting_code", "accounting_category1", "accounting_category2", "accounting_category3", "accounting_category4"]
      pass

    fields = ["id", "name", "item_family_id", "item_id", "description", "status", "external_name", \
    "pricing_model", "price", "price_in_decimal", "period", "currency_code", "period_unit", "trial_period", \
    "trial_period_unit", "trial_end_action", "shipping_period", "shipping_period_unit", "billing_cycles", \
    "free_quantity", "free_quantity_in_decimal", "resource_version", "updated_at", "created_at", \
    "archived_at", "invoice_notes", "tiers", "is_taxable", "tax_detail", "accounting_detail", "metadata", \
    "item_type", "archivable", "parent_item_id", "show_description_in_invoices", "show_description_in_quotes"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("item_prices"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("item_prices",id), None, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("item_prices",id), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("item_prices"), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("item_prices",id,"delete"), None, env, headers)

    @staticmethod
    def find_applicable_items(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("item_prices",id,"applicable_items"), params, env, headers)

    @staticmethod
    def find_applicable_item_prices(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("item_prices",id,"applicable_item_prices"), params, env, headers)
