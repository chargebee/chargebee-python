import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Order(Model):

    fields = ["id", "invoice_id", "status", "reference_id", "fulfillment_status", "note", "tracking_id", \
    "batch_id", "created_by", "created_at", "status_update_at"]


    @staticmethod
    def create(params, env=None):
        return request.send('post', request.uri_path("orders"), params, env)

    @staticmethod
    def update(id, params=None, env=None):
        return request.send('post', request.uri_path("orders",id), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("orders",id), None, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', request.uri_path("orders"), params, env)

    @staticmethod
    def orders_for_invoice(id, params=None, env=None):
        return request.send('get', request.uri_path("invoices",id,"orders"), params, env)
