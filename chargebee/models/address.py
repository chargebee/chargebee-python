from chargebee.model import Model
from chargebee import request


class Address(Model):

    @staticmethod
    def update(**params):
        return request.send('post', '/addresses', params)

    @staticmethod
    def retrieve(**params):
        return request.send('get', '/addresses', params)
