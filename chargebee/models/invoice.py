import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Invoice(Model):
    class LineItem(Model):
      fields = ["date_from", "date_to", "unit_amount", "quantity", "tax", "tax_rate", "amount", "description", "type", "entity_type", "entity_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "type", "entity_id"]
      pass
    class Tax(Model):
      fields = ["amount", "description"]
      pass
    class LinkedTransaction(Model):
      fields = ["txn_id", "applied_amount", "txn_type", "txn_status", "txn_date", "txn_amount"]
      pass

    fields = ["id", "customer_id", "subscription_id", "recurring", "status", "vat_number", \
    "start_date", "end_date", "amount", "paid_on", "next_retry", "sub_total", "tax", "line_items", \
    "discounts", "taxes", "linked_transactions"]


    @staticmethod
    def charge(params, env=None):
        return request.send('post', request.uri_path("invoices","charge"), params, env)

    @staticmethod
    def charge_addon(params, env=None):
        return request.send('post', request.uri_path("invoices","charge_addon"), params, env)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', request.uri_path("invoices"), params, env)

    @staticmethod
    def invoices_for_customer(id, params=None, env=None):
        return request.send('get', request.uri_path("customers",id,"invoices"), params, env)

    @staticmethod
    def invoices_for_subscription(id, params=None, env=None):
        return request.send('get', request.uri_path("subscriptions",id,"invoices"), params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("invoices",id), None, env)

    @staticmethod
    def pdf(id, env=None):
        return request.send('post', request.uri_path("invoices",id,"pdf"), None, env)

    @staticmethod
    def add_charge(id, params, env=None):
        return request.send('post', request.uri_path("invoices",id,"add_charge"), params, env)

    @staticmethod
    def add_addon_charge(id, params, env=None):
        return request.send('post', request.uri_path("invoices",id,"add_addon_charge"), params, env)

    @staticmethod
    def collect(id, env=None):
        return request.send('post', request.uri_path("invoices",id,"collect"), None, env)

    @staticmethod
    def refund(id, params=None, env=None):
        return request.send('post', request.uri_path("invoices",id,"refund"), params, env)
