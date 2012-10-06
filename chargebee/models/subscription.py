from chargebee.model import Model
from chargebee import request


class Subscription(Model):

    class Addon(Model):
        pass

    @staticmethod
    def create(**params):
        return request.send('post', '/subscriptions', params)

    @staticmethod
    def list(**params):
        return request.send('get', '/subscriptions', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/subscriptions/%s' % id, params)

    @staticmethod
    def update(id, **params):
        return request.send('post', '/subscriptions/%s' % id, params)

    @staticmethod
    def cancel(id, **params):
        return request.send('post', '/subscriptions/%s/cancel' % id, params)

    @staticmethod
    def reactivate(id, **params):
        return request.send('post', '/subscriptions/%s/reactivate' % id, params)
