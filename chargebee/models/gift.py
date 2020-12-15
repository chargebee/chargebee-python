import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Gift(Model):
    class Gifter(Model):
      fields = ["customer_id", "invoice_id", "signature", "note"]
      pass
    class GiftReceiver(Model):
      fields = ["customer_id", "subscription_id", "first_name", "last_name", "email"]
      pass
    class GiftTimeline(Model):
      fields = ["status", "occurred_at"]
      pass

    fields = ["id", "status", "scheduled_at", "auto_claim", "no_expiry", "claim_expiry_date", \
    "resource_version", "updated_at", "gifter", "gift_receiver", "gift_timelines"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("gifts"), params, env, headers)

    @staticmethod
    def create_for_items(params, env=None, headers=None):
        return request.send('post', request.uri_path("gifts","create_for_items"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("gifts",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("gifts"), params, env, headers)

    @staticmethod
    def claim(id, env=None, headers=None):
        return request.send('post', request.uri_path("gifts",id,"claim"), None, env, headers)

    @staticmethod
    def cancel(id, env=None, headers=None):
        return request.send('post', request.uri_path("gifts",id,"cancel"), None, env, headers)

    @staticmethod
    def update_gift(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("gifts",id,"update_gift"), params, env, headers)
