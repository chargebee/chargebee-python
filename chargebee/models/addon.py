import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Addon(Model):

    fields = ["id", "name", "invoice_name", "description", "type", "charge_type", "price", \
    "period", "period_unit", "unit", "status", "archived_at"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', request.uri_path("addons"), params, env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', request.uri_path("addons",id), params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', request.uri_path("addons"), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("addons",id), None, env)

    @staticmethod
    def delete(id, env=None):
        return request.send('post', request.uri_path("addons",id,"delete"), None, env)
