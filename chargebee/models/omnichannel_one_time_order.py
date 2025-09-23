import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelOneTimeOrder(Model):

    fields = ["id", "app_id", "customer_id", "id_at_source", "origin", "source", "created_at", \
    "resource_version", "omnichannel_one_time_order_items", "purchase_transaction"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("omnichannel_one_time_orders",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("omnichannel_one_time_orders"), params, env, headers, None, False,json_keys)
