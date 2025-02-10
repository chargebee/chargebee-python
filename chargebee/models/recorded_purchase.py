import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class RecordedPurchase(Model):
    class LinkedOmnichannelSubscription(Model):
      fields = ["omnichannel_subscription_id"]
      pass
    class ErrorDetail(Model):
      fields = ["error_message"]
      pass

    fields = ["id", "customer_id", "app_id", "source", "status", "omnichannel_transaction_id", \
    "created_at", "resource_version", "linked_omnichannel_subscriptions", "error_detail"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("recorded_purchases"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("recorded_purchases",id), None, env, headers, None, False,json_keys)
