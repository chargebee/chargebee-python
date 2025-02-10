import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class InAppSubscription(Model):

    fields = ["app_id", "subscription_id", "customer_id", "plan_id", "store_status", "invoice_id"]


    @staticmethod
    def process_receipt(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("in_app_subscriptions",id,"process_purchase_command"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_receipt(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("in_app_subscriptions",id,"import_receipt"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_subscription(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("in_app_subscriptions",id,"import_subscription"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve_store_subs(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("in_app_subscriptions",id,"retrieve"), params, env, headers, None, False,json_keys)
