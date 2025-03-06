import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Purchase(Model):

    fields = ["id", "customer_id", "created_at", "modified_at", "subscription_ids", "invoice_ids"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
            "meta_data": 1,
        }
        return request.send('post', request.uri_path("purchases"), params, env, headers, None, False,json_keys)

    @staticmethod
    def estimate(params, env=None, headers=None):
        json_keys = { 
            "exemption_details": 1,
        }
        return request.send('post', request.uri_path("purchases","estimate"), params, env, headers, None, False,json_keys)
