import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Entitlement(Model):

    fields = ["id", "entity_id", "entity_type", "feature_id", "feature_name", "value", "name"]


    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("entitlements"), params, env, headers)

    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("entitlements"), params, env, headers)
