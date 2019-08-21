import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Plan(Model):
    class Tier(Model):
      fields = ["starting_unit", "ending_unit", "price"]
      pass
    class ApplicableAddon(Model):
      fields = ["id"]
      pass
    class AttachedAddon(Model):
      fields = ["id", "quantity", "billing_cycles", "type"]
      pass
    class EventBasedAddon(Model):
      fields = ["id", "quantity", "on_event", "charge_once"]
      pass

    fields = ["id", "name", "invoice_name", "description", "price", "currency_code", "period", \
    "period_unit", "trial_period", "trial_period_unit", "pricing_model", "charge_model", "free_quantity", \
    "setup_cost", "downgrade_penalty", "status", "archived_at", "billing_cycles", "redirect_url", \
    "enabled_in_hosted_pages", "enabled_in_portal", "addon_applicability", "tax_code", "avalara_sale_type", \
    "avalara_transaction_type", "avalara_service_type", "sku", "accounting_code", "accounting_category1", \
    "accounting_category2", "is_shippable", "shipping_frequency_period", "shipping_frequency_period_unit", \
    "resource_version", "updated_at", "giftable", "claim_url", "invoice_notes", "taxable", "tax_profile_id", \
    "meta_data", "tiers", "applicable_addons", "attached_addons", "event_based_addons"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("plans"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("plans",id), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("plans"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("plans",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("plans",id,"delete"), None, env, headers)

    @staticmethod
    def copy(params, env=None, headers=None):
        return request.send('post', request.uri_path("plans","copy"), params, env, headers)

    @staticmethod
    def unarchive(id, env=None, headers=None):
        return request.send('post', request.uri_path("plans",id,"unarchive"), None, env, headers)
