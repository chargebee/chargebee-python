import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Plan(Model):


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/plans', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/plans/%s' % id, None, env)
