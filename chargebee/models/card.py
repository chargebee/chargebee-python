from chargebee.model import Model
from chargebee import request


class Card(Model):

    def retrieve(self, id, env=None):
        return request.send('get', '/cards/%s' % id, {}, env)

    def update_card_for_customer(self, id, params, env=None):
        return request.send('post', '/customers/%s/credit_card' % id, params, env)
