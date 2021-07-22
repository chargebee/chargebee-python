import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Usage(Model):

    fields = ["id", "usage_date", "subscription_id", "item_price_id", "invoice_id", "line_item_id", \
    "quantity", "source", "note", "resource_version", "updated_at", "created_at"]


    @staticmethod
    def create(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"usages"), params, env, headers)

    @staticmethod
    def retrieve(id, params, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"usages"), params, env, headers)

    @staticmethod
    def delete(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"delete_usage"), params, env, headers)

    @staticmethod
    def list(params, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("usages"), params, env, headers)

    @staticmethod
    def pdf(params, env=None, headers=None):
        return request.send('post', request.uri_path("usages","pdf"), params, env, headers)
