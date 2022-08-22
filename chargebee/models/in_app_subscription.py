import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class InAppSubscription(Model):

    fields = ["app_id", "subscription_id", "customer_id", "plan_id"]


    @staticmethod
    def process_receipt(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("in_app_subscriptions",id,"process_purchase_command"), params, env, headers)

    @staticmethod
    def import_receipt(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("in_app_subscriptions",id,"import_receipt"), params, env, headers)
