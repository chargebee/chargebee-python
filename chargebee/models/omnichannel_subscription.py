import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelSubscription(Model):
    class OmnichannelSubscriptionItem(Model):
      fields = ["id", "id_at_source", "status", "current_term_start", "current_term_end", "expired_at", "expiration_reason", "cancelled_at", "cancellation_reason"]
      pass

    fields = ["id", "id_at_source", "app_id", "source", "customer_id", "created_at", "omnichannel_subscription_items"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("omnichannel_subscriptions",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("omnichannel_subscriptions"), params, env, headers)

    @staticmethod
    def omnichannel_transactions_for_omnichannel_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("omnichannel_subscriptions",id,"omnichannel_transactions"), params, env, headers)
