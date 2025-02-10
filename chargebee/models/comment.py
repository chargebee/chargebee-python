import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Comment(Model):

    fields = ["id", "entity_type", "added_by", "notes", "created_at", "type", "entity_id"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("comments"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("comments",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("comments"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("comments",id,"delete"), None, env, headers, None, False,json_keys)
