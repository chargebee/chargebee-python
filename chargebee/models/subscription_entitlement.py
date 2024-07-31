import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SubscriptionEntitlement(Model):
    class Component(Model):
      fields = ["entitlement_overrides"]
      pass

    fields = ["subscription_id", "feature_id", "feature_name", "feature_unit", "value", "name", \
    "is_overridden", "is_enabled", "effective_from", "schedule_status", "expires_at", "components"]


    @staticmethod
    def subscription_entitlements_for_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"subscription_entitlements"), params, env, headers)

    @staticmethod
    def set_subscription_entitlement_availability(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"subscription_entitlements/set_availability"), params, env, headers)
