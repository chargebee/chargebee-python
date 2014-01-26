import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Addon(Model):

    fields = ["id", "name", "invoice_name", "type", "charge_type", "price", "period", "period_unit", \
    "unit", "status", "archived_at"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', '/addons', params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/addons', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/addons/%s' % id, None, env)
