import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Currency(Model):

    fields = ["id", "enabled", "forex_type", "currency_code", "is_base_currency", "manual_exchange_rate"]


    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("currencies","list"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("currencies",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("currencies"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("currencies",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_schedule(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("currencies",id,"add_schedule"), params, env, headers, None, False,json_keys)

    @staticmethod
    def remove_schedule(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("currencies",id,"remove_schedule"), None, env, headers, None, False,json_keys)
