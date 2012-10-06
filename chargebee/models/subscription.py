from chargebee.model import Model
from chargebee import request


class Subscription(Model):

    class Addon(Model):
        pass

    @staticmethod
    def create(params, env=None):
        return request.send('post', '/subscriptions', params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/subscriptions', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/subscriptions/%s' % id, env=env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', '/subscriptions/%s' % id, params, env)

    @staticmethod
    def cancel(id, params=None, env=None):
        return request.send('post', '/subscriptions/%s/cancel' % id, params, env)

    @staticmethod
    def reactivate(id, params=None, env=None):
        return request.send('post', '/subscriptions/%s/reactivate' % id, params, env)
