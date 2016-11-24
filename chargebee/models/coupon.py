import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Coupon(Model):

    fields = ["id", "name", "invoice_name", "discount_type", "discount_percentage", "discount_amount", \
    "discount_quantity", "currency_code", "duration_type", "duration_month", "valid_till", "max_redemptions", \
    "status", "apply_discount_on", "apply_on", "plan_constraint", "addon_constraint", "created_at", \
    "archived_at", "resource_version", "updated_at", "plan_ids", "addon_ids", "redemptions", "invoice_notes", \
    "meta_data"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("coupons"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("coupons"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("coupons",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("coupons",id,"delete"), None, env, headers)

    @staticmethod
    def copy(params, env=None, headers=None):
        return request.send('post', request.uri_path("coupons","copy"), params, env, headers)
