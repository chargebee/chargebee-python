import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Rule(Model):

    fields = ["id", "namespace", "rule_name", "rule_order", "status", "conditions", "outcome", \
    "deleted", "created_at", "modified_at"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("rules",id), None, env, headers, None, False,json_keys)
