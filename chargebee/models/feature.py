import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Feature(Model):
    class Level(Model):
      fields = ["name", "value", "level", "is_unlimited"]
      pass

    fields = ["id", "name", "description", "status", "type", "unit", "resource_version", "updated_at", \
    "created_at", "levels"]


    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("features"), params, env, headers)

    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("features"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("features",id), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("features",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("features",id,"delete"), None, env, headers)

    @staticmethod
    def activate(id, env=None, headers=None):
        return request.send('post', request.uri_path("features",id,"activate_command"), None, env, headers)

    @staticmethod
    def archive(id, env=None, headers=None):
        return request.send('post', request.uri_path("features",id,"archive_command"), None, env, headers)

    @staticmethod
    def reactivate(id, env=None, headers=None):
        return request.send('post', request.uri_path("features",id,"reactivate_command"), None, env, headers)
