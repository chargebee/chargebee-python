from chargebee.model import Model
from chargebee import request


class Plan(Model):

    @staticmethod
    def list(**params):
        return request.send('get', '/plans', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/plans/%s' % id, params)
