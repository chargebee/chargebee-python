import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Address(Model):


    @staticmethod
    def update(params, env=None):
        return request.send('post', '/addresses', params, env)

    @staticmethod
    def retrieve(params, env=None):
        return request.send('get', '/addresses', params, env)
