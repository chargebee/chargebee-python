import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Plan(Model):

    fields = ["id", "name", "invoice_name", "description", "price", "currency_code", "period", \
    "period_unit", "trial_period", "trial_period_unit", "charge_model", "free_quantity", "setup_cost", \
    "downgrade_penalty", "status", "archived_at", "billing_cycles", "redirect_url", "enabled_in_hosted_pages", \
    "enabled_in_portal", "tax_code", "sku", "accounting_code", "accounting_category1", "accounting_category2", \
    "resource_version", "updated_at", "invoice_notes", "taxable", "tax_profile_id", "meta_data"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("plans"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("plans",id), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("plans"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("plans",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("plans",id,"delete"), None, env, headers)

    @staticmethod
    def copy(params, env=None, headers=None):
        return request.send('post', request.uri_path("plans","copy"), params, env, headers)
