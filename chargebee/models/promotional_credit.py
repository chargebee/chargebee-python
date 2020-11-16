import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PromotionalCredit(Model):

    fields = ["id", "customer_id", "type", "amount_in_decimal", "amount", "currency_code", \
    "description", "credit_type", "reference", "closing_balance", "done_by", "created_at"]


    @staticmethod
    def add(params, env=None, headers=None):
        return request.send('post', request.uri_path("promotional_credits","add"), params, env, headers)

    @staticmethod
    def deduct(params, env=None, headers=None):
        return request.send('post', request.uri_path("promotional_credits","deduct"), params, env, headers)

    @staticmethod
    def set(params, env=None, headers=None):
        return request.send('post', request.uri_path("promotional_credits","set"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("promotional_credits"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("promotional_credits",id), None, env, headers)
