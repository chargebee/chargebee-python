import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Plan(Model):

    fields = ["id", "name", "invoice_name", "price", "period", "period_unit", "trial_period", \
    "trial_period_unit", "free_quantity", "setup_cost", "downgrade_penalty", "status", "archived_at", \
    "billing_cycles", "redirect_url"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', '/plans', params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/plans', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/plans/%s' % id, None, env)
