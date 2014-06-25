import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PortalSession(Model):

    fields = ["id", "access_url", "redirect_url", "status", "created_at", "expires_at", "customer_id", \
    "login_at", "logout_at", "login_ipaddress", "logout_ipaddress"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', request.uri_path("portal_sessions"), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("portal_sessions",id), None, env)

    @staticmethod
    def logout(id, env=None):
        return request.send('post', request.uri_path("portal_sessions",id,"logout"), None, env)
