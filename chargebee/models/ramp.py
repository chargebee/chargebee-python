import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Ramp(Model):
    class ItemsToAdd(Model):
      fields = ["item_price_id", "item_type", "quantity", "quantity_in_decimal", "unit_price", "unit_price_in_decimal", "amount", "amount_in_decimal", "free_quantity", "free_quantity_in_decimal", "billing_cycles", "service_period_days", "metered_quantity", "charge_once", "charge_on_option", "charge_on_event"]
      pass
    class ItemsToUpdate(Model):
      fields = ["item_price_id", "item_type", "quantity", "quantity_in_decimal", "unit_price", "unit_price_in_decimal", "amount", "amount_in_decimal", "free_quantity", "free_quantity_in_decimal", "billing_cycles", "service_period_days", "metered_quantity", "charge_once", "charge_on_option", "charge_on_event"]
      pass
    class CouponsToAdd(Model):
      fields = ["coupon_id", "apply_till"]
      pass
    class DiscountsToAdd(Model):
      fields = ["id", "invoice_name", "type", "percentage", "amount", "duration_type", "period", "period_unit", "included_in_mrr", "apply_on", "item_price_id", "created_at"]
      pass
    class ItemTier(Model):
      fields = ["item_price_id", "starting_unit", "ending_unit", "price", "starting_unit_in_decimal", "ending_unit_in_decimal", "price_in_decimal", "pricing_type", "package_size", "index"]
      pass
    class ContractTerm(Model):
      fields = ["cancellation_cutoff_period", "renewal_billing_cycles", "action_at_term_end"]
      pass
    class StatusTransitionReason(Model):
      fields = ["code", "message"]
      pass

    fields = ["id", "description", "subscription_id", "effective_from", "status", "created_at", \
    "resource_version", "updated_at", "items_to_add", "items_to_update", "coupons_to_add", "discounts_to_add", \
    "item_tiers", "items_to_remove", "coupons_to_remove", "discounts_to_remove", "contract_term", \
    "deleted", "status_transition_reason"]


    @staticmethod
    def create_for_subscription(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"create_ramp"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("ramps",id,"update"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("ramps",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("ramps",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("ramps"), params, env, headers, None, False,json_keys)
