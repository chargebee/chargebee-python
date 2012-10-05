from chargebee.model import Model
from chargebee import request


class Plan(Model):

    def list(self, params, env=None):
        return request.send('get', '/plans', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/plans/%s' % id, {}, env)
