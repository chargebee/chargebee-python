import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OfflineCheckout(Model):


    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/offline_checkouts/%s' % id, None, env)

    @staticmethod
    def pre_register(params, env=None):
        return request.send('post', '/offline_checkouts/pre_register', params, env)

    @staticmethod
    def post_register(id, params, env=None):
        return request.send('post', '/offline_checkouts/%s/post_register' % id, params, env)
