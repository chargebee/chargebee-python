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
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip"]
      pass

    fields = ["id", "plan_id", "plan_quantity", "status", "start_date", "trial_start", "trial_end", \
    "current_term_start", "current_term_end", "remaining_billing_cycles", "created_at", "started_at", \
    "activated_at", "cancelled_at", "cancel_reason", "affiliate_token", "created_from_ip", "due_invoices_count", \
    "due_since", "total_dues", "addons", "coupon", "coupons", "shipping_address", "has_scheduled_changes"]


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
    def retrieve_with_scheduled_changes(id, env=None):
        return request.send('get', request.uri_path("subscriptions",id,"retrieve_with_scheduled_changes"), None, env)

    @staticmethod
    def remove_scheduled_changes(id, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_changes"), None, env)

    @staticmethod
    def remove_scheduled_cancellation(id, params=None, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_cancellation"), params, env)

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
    def add_charge_at_term_end(id, params, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"add_charge_at_term_end"), params, env)

    @staticmethod
    def charge_addon_at_term_end(id, params, env=None):
        return request.send('post', request.uri_path("subscriptions",id,"charge_addon_at_term_end"), params, env)
