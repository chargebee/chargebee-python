import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Estimate(Model):

    fields = ["created_at", "subscription_estimate", "invoice_estimate", "credit_note_estimates"]


    @staticmethod
    def create_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("estimates","create_subscription"), params, env, headers)

    @staticmethod
    def update_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("estimates","update_subscription"), params, env, headers)

    @staticmethod
    def renewal_estimate(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"renewal_estimate"), params, env, headers)
