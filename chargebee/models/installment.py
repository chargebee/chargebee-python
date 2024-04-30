import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Installment(Model):

    fields = ["id", "invoice_id", "date", "amount", "status", "created_at", "resource_version", \
    "updated_at"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("installments",id), None, env, headers)

    @staticmethod
    def list(params, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("installments"), params, env, headers)
