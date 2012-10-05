from chargebee.model import Model
from chargebee import request


class Address(Model):

    def update(self, params, env=None):
        return request.send('post', '/addresses', params, env)

    def retrieve(self, params, env=None):
        return request.send('get', '/addresses', params, env)
