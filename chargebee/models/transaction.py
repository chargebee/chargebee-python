import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Transaction(Model):


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/transactions', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/transactions/%s' % id, None, env)

    @staticmethod
    def transactions_for_subscription(id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/transactions' % id, params, env)
