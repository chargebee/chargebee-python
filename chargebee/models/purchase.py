import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Purchase(Model):

    fields = ["id", "customer_id", "created_at", "modified_at", "subscription_ids", "invoice_ids"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("purchases"), params, env, headers)

    @staticmethod
    def estimate(params, env=None, headers=None):
        return request.send('post', request.uri_path("purchases","estimate"), params, env, headers)
