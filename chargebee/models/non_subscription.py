import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class NonSubscription(Model):

    fields = ["app_id", "invoice_id", "customer_id", "charge_id"]


    @staticmethod
    def process_receipt(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("non_subscriptions",id,"one_time_purchase"), params, env, headers, None, False,json_keys)
