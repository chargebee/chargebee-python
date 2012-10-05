from chargebee.model import Model
from chargebee import request


class Customer(Model):

    def list(self, params=None, env=None):
        return request.send('get', '/customers', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/customers/%s' % id, {}, env)

    def update(self, id, params=None, env=None):
        return request.send('post', '/customers/%s' % id, params, env)
