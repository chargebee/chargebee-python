import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Plan(Model):
    class Tier(Model):
      fields = ["starting_unit", "ending_unit", "price", "starting_unit_in_decimal", "ending_unit_in_decimal", "price_in_decimal", "pricing_type", "package_size"]
      pass
    class TaxProvidersField(Model):
      fields = ["provider_name", "field_id", "field_value"]
      pass
    class ApplicableAddon(Model):
      fields = ["id"]
      pass
    class AttachedAddon(Model):
      fields = ["id", "quantity", "billing_cycles", "type", "quantity_in_decimal"]
      pass
    class EventBasedAddon(Model):
      fields = ["id", "quantity", "on_event", "charge_once", "quantity_in_decimal"]
      pass

    fields = ["id", "name", "invoice_name", "description", "price", "currency_code", "period", \
    "period_unit", "trial_period", "trial_period_unit", "trial_end_action", "pricing_model", "charge_model", \
    "free_quantity", "setup_cost", "downgrade_penalty", "status", "archived_at", "billing_cycles", \
    "redirect_url", "enabled_in_hosted_pages", "enabled_in_portal", "addon_applicability", "tax_code", \
    "hsn_code", "taxjar_product_code", "avalara_sale_type", "avalara_transaction_type", "avalara_service_type", \
    "sku", "accounting_code", "accounting_category1", "accounting_category2", "accounting_category3", \
    "accounting_category4", "is_shippable", "shipping_frequency_period", "shipping_frequency_period_unit", \
    "resource_version", "updated_at", "giftable", "claim_url", "free_quantity_in_decimal", "price_in_decimal", \
    "channel", "invoice_notes", "taxable", "tax_profile_id", "meta_data", "tiers", "tax_providers_fields", \
    "applicable_addons", "attached_addons", "event_based_addons", "show_description_in_invoices", \
    "show_description_in_quotes"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("plans"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("plans",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("plans"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("plans",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("plans",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def copy(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("plans","copy"), params, env, headers, None, False,json_keys)

    @staticmethod
    def unarchive(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("plans",id,"unarchive"), None, env, headers, None, False,json_keys)
