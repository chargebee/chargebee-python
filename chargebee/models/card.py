import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Card(Model):


    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/cards/%s' % id, None, env)

    @staticmethod
    def update_card_for_customer(id, params, env=None):
        return request.send('post', '/customers/%s/credit_card' % id, params, env)
