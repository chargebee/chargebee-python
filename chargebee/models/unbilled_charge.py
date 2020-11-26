import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class UnbilledCharge(Model):
    class Tier(Model):
      fields = ["starting_unit", "ending_unit", "quantity_used", "unit_amount", "starting_unit_in_decimal", "ending_unit_in_decimal", "quantity_used_in_decimal", "unit_amount_in_decimal"]
      pass

    fields = ["id", "customer_id", "subscription_id", "date_from", "date_to", "unit_amount", \
    "pricing_model", "quantity", "amount", "currency_code", "discount_amount", "description", "entity_type", \
    "entity_id", "is_voided", "voided_at", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", \
    "tiers", "deleted"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("unbilled_charges"), params, env, headers)

    @staticmethod
    def invoice_unbilled_charges(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("unbilled_charges","invoice_unbilled_charges"), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("unbilled_charges",id,"delete"), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("unbilled_charges"), params, env, headers)

    @staticmethod
    def invoice_now_estimate(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("unbilled_charges","invoice_now_estimate"), params, env, headers)
