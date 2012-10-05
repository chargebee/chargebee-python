from chargebee.model import Model
from chargebee import request


class Coupon(Model):

    def list(self, params=None, env=None):
        return request.send('get', '/coupons', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/coupons/%s' % id, {}, env)
