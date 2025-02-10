import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class UsageEvent(Model):

    fields = ["subscription_id", "deduplication_id", "usage_timestamp", "properties"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
            "properties": 0,
        }
        return request.send('post', request.uri_path("usage_events"), params, env, headers, "ingest", True,json_keys)

    @staticmethod
    def batch_ingest(params, env=None, headers=None):
        json_keys = { 
            "properties": 1,
        }
        return request.send('post', request.uri_path("batch","usage_events"), params, env, headers, "ingest", True,json_keys)
