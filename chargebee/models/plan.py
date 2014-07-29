import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Plan(Model):

    fields = ["id", "name", "invoice_name", "description", "price", "period", "period_unit", \
    "trial_period", "trial_period_unit", "charge_model", "free_quantity", "setup_cost", "downgrade_penalty", \
    "status", "archived_at", "billing_cycles", "redirect_url", "enabled_in_hosted_pages"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', request.uri_path("plans"), params, env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', request.uri_path("plans",id), params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', request.uri_path("plans"), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("plans",id), None, env)

    @staticmethod
    def delete(id, env=None):
        return request.send('post', request.uri_path("plans",id,"delete"), None, env)
