import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class VirtualBankAccount(Model):

    fields = ["id", "customer_id", "email", "scheme", "bank_name", "account_number", "routing_number", \
    "swift_code", "gateway", "gateway_account_id", "resource_version", "updated_at", "created_at", \
    "reference_id", "deleted"]


    @staticmethod
    def create_using_permanent_token(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("virtual_bank_accounts","create_using_permanent_token"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("virtual_bank_accounts"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("virtual_bank_accounts",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("virtual_bank_accounts"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("virtual_bank_accounts",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete_local(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("virtual_bank_accounts",id,"delete_local"), None, env, headers, None, False,json_keys)
