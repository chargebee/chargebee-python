import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class WebhookEndpoint(Model):

    fields = ["id", "name", "url", "send_card_resource", "disabled", "primary_url", "api_version", \
    "chargebee_response_schema_type", "enabled_events"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("webhook_endpoints"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("webhook_endpoints",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("webhook_endpoints",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("webhook_endpoints",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("webhook_endpoints"), params, env, headers, None, False,json_keys)
