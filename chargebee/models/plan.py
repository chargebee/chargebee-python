from chargebee.model import Model
from chargebee import request


class Plan(Model):

    @staticmethod
    def list(params, env=None):
        return request.send('get', '/plans', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/plans/%s' % id, {}, env)
