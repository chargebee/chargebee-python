import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Customer(Model):
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state", "country", "zip"]
      pass

    fields = ["id", "first_name", "last_name", "email", "phone", "company", "vat_number", "auto_collection", \
    "created_at", "card_status", "billing_address"]


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/customers', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/customers/%s' % id, None, env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', '/customers/%s' % id, params, env)

    @staticmethod
    def update_billing_info(id, params=None, env=None):
        return request.send('post', '/customers/%s/update_billing_info' % id, params, env)
