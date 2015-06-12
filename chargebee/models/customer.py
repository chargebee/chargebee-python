import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Customer(Model):
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip"]
      pass
    class PaymentMethod(Model):
      fields = ["type", "status", "reference_id"]
      pass

    fields = ["id", "first_name", "last_name", "email", "phone", "company", "vat_number", "auto_collection", \
    "created_at", "created_from_ip", "card_status", "billing_address", "payment_method", "invoice_notes", \
    "account_credits"]


    @staticmethod
    def create(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id), None, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id), params, env, headers)

    @staticmethod
    def update_payment_method(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"update_payment_method"), params, env, headers)

    @staticmethod
    def update_billing_info(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"update_billing_info"), params, env, headers)

    @staticmethod
    def add_account_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"add_account_credits"), params, env, headers)

    @staticmethod
    def deduct_account_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"deduct_account_credits"), params, env, headers)

    @staticmethod
    def set_account_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"set_account_credits"), params, env, headers)
