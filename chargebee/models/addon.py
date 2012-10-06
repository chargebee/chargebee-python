from chargebee.model import Model
from chargebee import request


class Addon(Model):

    @staticmethod
    def list(**params):
        return request.send('get', '/addons', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/addons/%s' % id, params)
