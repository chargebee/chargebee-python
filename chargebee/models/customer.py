import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Customer(Model):


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/customers', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/customers/%s' % id, None, env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', '/customers/%s' % id, params, env)
