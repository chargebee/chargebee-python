import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Coupon(Model):

    fields = ["id", "name", "invoice_name", "discount_type", "discount_percentage", "discount_amount", \
    "discount_quantity", "duration_type", "duration_month", "max_redemptions", "status", "redemptions", \
    "apply_discount_on", "apply_on", "created_at", "archived_at", "valid_till"]


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/coupons', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/coupons/%s' % id, None, env)
