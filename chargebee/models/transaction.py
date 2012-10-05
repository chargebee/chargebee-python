from chargebee.model import Model
from chargebee import request


class Transaction(Model):

    def list(self, params=None, env=None):
        return request.send('get', '/transactions', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/transactions/%s' % id, {}, env)

    def transactions_for_subscription(self, id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/transactions' % id, params, env)
