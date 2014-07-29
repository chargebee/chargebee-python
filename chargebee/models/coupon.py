import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Coupon(Model):

    fields = ["id", "name", "invoice_name", "discount_type", "discount_percentage", "discount_amount", \
    "discount_quantity", "duration_type", "duration_month", "valid_till", "max_redemptions", "status", \
    "apply_discount_on", "apply_on", "plan_constraint", "addon_constraint", "created_at", "archived_at", \
    "plan_ids", "addon_ids", "redemptions"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', request.uri_path("coupons"), params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', request.uri_path("coupons"), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("coupons",id), None, env)
