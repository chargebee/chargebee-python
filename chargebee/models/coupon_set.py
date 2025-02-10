import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CouponSet(Model):

    fields = ["id", "coupon_id", "name", "total_count", "redeemed_count", "archived_count", \
    "meta_data"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("coupon_sets"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_coupon_codes(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("coupon_sets",id,"add_coupon_codes"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("coupon_sets"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("coupon_sets",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("coupon_sets",id,"update"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("coupon_sets",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete_unused_coupon_codes(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("coupon_sets",id,"delete_unused_coupon_codes"), None, env, headers, None, False,json_keys)
