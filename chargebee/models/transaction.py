from chargebee.model import Model
from chargebee import request


class Transaction(Model):

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/transactions', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/transactions/%s' % id, {}, env)

    @staticmethod
    def transactions_for_subscription(id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/transactions' % id, params, env)
