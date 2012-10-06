from chargebee.model import Model
from chargebee import request


class Customer(Model):

    @staticmethod
    def list(**params):
        return request.send('get', '/customers', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/customers/%s' % id, params)

    @staticmethod
    def update(id, **params):
        return request.send('post', '/customers/%s' % id, params)
