from chargebee.model import Model
from chargebee import request


class Subscription(Model):

    class Addon(Model):
        pass

    def create(self, params, env=None):
        return request.send('post', '/subscriptions', params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/subscriptions', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/subscriptions/%s' % id, env=env)

    def update(self, id, params=None, env=None):
        return request.send('post', '/subscriptions/%s' % id, params, env)

    def cancel(self, id, params=None, env=None):
        return request.send('post', '/subscriptions/%s/cancel' % id, params, env)

    def reactivate(self, id, params=None, env=None):
        return request.send('post', '/subscriptions/%s/reactivate' % id, params, env)
