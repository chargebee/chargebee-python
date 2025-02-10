import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelSubscription(Model):
    class OmnichannelTransaction(Model):
      fields = ["id", "id_at_source", "app_id", "price_currency", "price_units", "price_nanos", "type", "transacted_at", "created_at", "resource_version"]
      pass

    fields = ["id", "id_at_source", "app_id", "source", "customer_id", "created_at", "resource_version", \
    "omnichannel_subscription_items", "initial_purchase_transaction"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("omnichannel_subscriptions",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("omnichannel_subscriptions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def omnichannel_transactions_for_omnichannel_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("omnichannel_subscriptions",id,"omnichannel_transactions"), params, env, headers, None, False,json_keys)
