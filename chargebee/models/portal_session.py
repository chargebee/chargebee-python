import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PortalSession(Model):
    class LinkedCustomer(Model):
      fields = ["customer_id", "email", "has_billing_address", "has_payment_method", "has_active_subscription"]
      pass

    fields = ["id", "token", "access_url", "redirect_url", "status", "created_at", "expires_at", \
    "customer_id", "login_at", "logout_at", "login_ipaddress", "logout_ipaddress", "linked_customers"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("portal_sessions"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("portal_sessions",id), None, env, headers)

    @staticmethod
    def logout(id, env=None, headers=None):
        return request.send('post', request.uri_path("portal_sessions",id,"logout"), None, env, headers)

    @staticmethod
    def activate(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("portal_sessions",id,"activate"), params, env, headers)
