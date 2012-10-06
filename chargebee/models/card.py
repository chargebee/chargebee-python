from chargebee.model import Model
from chargebee import request


class Card(Model):

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/cards/%s' % id, params)

    @staticmethod
    def update_card_for_customer(id, **params):
        return request.send('post', '/customers/%s/credit_card' % id, params)
