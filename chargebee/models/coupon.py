import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Coupon(Model):
    class ItemConstraint(Model):
      fields = ["item_type", "constraint", "item_price_ids"]
      pass
    class ItemConstraintCriteria(Model):
      fields = ["item_type", "currencies", "item_family_ids", "item_price_periods"]
      pass

    fields = ["id", "name", "invoice_name", "discount_type", "discount_percentage", "discount_amount", \
    "discount_quantity", "currency_code", "duration_type", "duration_month", "valid_till", "max_redemptions", \
    "status", "apply_discount_on", "apply_on", "plan_constraint", "addon_constraint", "created_at", \
    "archived_at", "resource_version", "updated_at", "included_in_mrr", "period", "period_unit", \
    "plan_ids", "addon_ids", "item_constraints", "item_constraint_criteria", "redemptions", "invoice_notes", \
    "meta_data"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("coupons"), params, env, headers)

    @staticmethod
    def create_for_items(params, env=None, headers=None):
        return request.send('post', request.uri_path("coupons","create_for_items"), params, env, headers)

    @staticmethod
    def update_for_items(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("coupons",id,"update_for_items"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("coupons"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("coupons",id), None, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("coupons",id), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("coupons",id,"delete"), None, env, headers)

    @staticmethod
    def copy(params, env=None, headers=None):
        return request.send('post', request.uri_path("coupons","copy"), params, env, headers)

    @staticmethod
    def unarchive(id, env=None, headers=None):
        return request.send('post', request.uri_path("coupons",id,"unarchive"), None, env, headers)
