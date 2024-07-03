import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PricingPageSession(Model):

    fields = ["id", "url", "created_at", "expires_at"]


    @staticmethod
    def create_for_new_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("pricing_page_sessions","create_for_new_subscription"), params, env, headers)

    @staticmethod
    def create_for_existing_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("pricing_page_sessions","create_for_existing_subscription"), params, env, headers)
