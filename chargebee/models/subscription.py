import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Subscription(Model):
    class Addon(Model):
      fields = ["id", "quantity"]
      pass
    class Coupon(Model):
      fields = ["coupon_id", "apply_till", "applied_count", "coupon_code"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state", "country", "zip"]
      pass

    fields = ["id", "plan_id", "plan_quantity", "status", "start_date", "trial_start", "trial_end", \
    "current_term_start", "current_term_end", "remaining_billing_cycles", "created_at", "started_at", \
    "activated_at", "cancelled_at", "cancel_reason", "due_invoices_count", "due_since", "total_dues", \
    "addons", "coupon", "coupons", "shipping_address"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', request.uri_path("subscriptions"), params, env)

    @staticmethod
    def create_for_customer(id, params, env=None):
        return request.send('post', request.uri_path("customers",id,"subscriptions"), params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', request.uri_path("subscriptions"), params, env)

    @staticmethod
    def subscriptions_for_customer(id, params=None, env=None):
        return request.send('get', request.uri_path("customers",id,"subscriptions"), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("subscriptions",id), None, env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', request.uri_path("subscriptions",id), params, env)

    @staticmethod
    def change_term_end(id, params, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"change_term_end"), params, env)

    @staticmethod
    def cancel(id, params=None, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"cancel"), params, env)

    @staticmethod
    def reactivate(id, params=None, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"reactivate"), params, env)

    @staticmethod
    def add_credit(id, params, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"add_credit"), params, env)
