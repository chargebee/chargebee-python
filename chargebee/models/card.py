import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Card(Model):

    fields = ["payment_source_id", "status", "gateway", "gateway_account_id", "ref_tx_id", \
    "first_name", "last_name", "iin", "last4", "card_type", "funding_type", "expiry_month", "expiry_year", \
    "issuing_country", "billing_addr1", "billing_addr2", "billing_city", "billing_state_code", "billing_state", \
    "billing_country", "billing_zip", "created_at", "resource_version", "updated_at", "ip_address", \
    "powered_by", "customer_id", "masked_number"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("cards",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def update_card_for_customer(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"credit_card"), params, env, headers, None, False,json_keys)

    @staticmethod
    def switch_gateway_for_customer(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"switch_gateway"), params, env, headers, None, False,json_keys)

    @staticmethod
    def copy_card_for_customer(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"copy_card"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete_card_for_customer(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"delete_card"), None, env, headers, None, False,json_keys)
