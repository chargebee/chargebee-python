from chargebee.model import Model
from chargebee import request


class Transaction(Model):

    @staticmethod
    def list(**params):
        return request.send('get', '/transactions', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/transactions/%s' % id, params)

    @staticmethod
    def transactions_for_subscription(id, **params):
        return request.send('get', '/subscriptions/%s/transactions' % id, params)
