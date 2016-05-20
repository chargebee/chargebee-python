import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Customer(Model):
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip"]
      pass
    class Contact(Model):
      fields = ["id", "first_name", "last_name", "email", "phone", "label", "enabled", "send_account_email", "send_billing_email"]
      pass
    class PaymentMethod(Model):
      fields = ["type", "gateway", "status", "reference_id"]
      pass

    fields = ["id", "first_name", "last_name", "email", "phone", "company", "vat_number", "auto_collection", \
    "allow_direct_debit", "created_at", "created_from_ip", "taxability", "entity_code", "exempt_number", \
    "card_status", "billing_address", "contacts", "payment_method", "invoice_notes", "promotional_credits", \
    "refundable_credits", "excess_payments", "meta_data"]


    @staticmethod
    def create(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("customers"), params, env, headers)

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
    def add_contact(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"add_contact"), params, env, headers)

    @staticmethod
    def update_contact(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"update_contact"), params, env, headers)

    @staticmethod
    def delete_contact(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"delete_contact"), params, env, headers)

    @staticmethod
    def add_promotional_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"add_promotional_credits"), params, env, headers)

    @staticmethod
    def deduct_promotional_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"deduct_promotional_credits"), params, env, headers)

    @staticmethod
    def set_promotional_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"set_promotional_credits"), params, env, headers)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"delete"), params, env, headers)
