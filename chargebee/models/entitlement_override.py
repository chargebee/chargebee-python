import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class EntitlementOverride(Model):

    fields = ["id", "entity_id", "entity_type", "feature_id", "feature_name", "value", "name", \
    "expires_at", "effective_from", "schedule_status"]


    @staticmethod
    def add_entitlement_override_for_subscription(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"entitlement_overrides"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list_entitlement_override_for_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"entitlement_overrides"), params, env, headers, None, False,json_keys)
