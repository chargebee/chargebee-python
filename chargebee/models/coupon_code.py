import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CouponCode(Model):

    fields = ["code", "status", "coupon_id", "coupon_set_id", "coupon_set_name"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("coupon_codes"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("coupon_codes",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("coupon_codes"), params, env, headers, None, False,json_keys)

    @staticmethod
    def archive(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("coupon_codes",id,"archive"), None, env, headers, None, False,json_keys)
