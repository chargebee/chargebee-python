import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Coupon(Model):


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/coupons', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/coupons/%s' % id, None, env)
