from chargebee.model import Model
from chargebee import request


class Coupon(Model):

    @staticmethod
    def list(**params):
        return request.send('get', '/coupons', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/coupons/%s' % id, params)
