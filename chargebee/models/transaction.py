import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Transaction(Model):
    class LinkedInvoice(Model):
      fields = ["invoice_id", "applied_amount", "invoice_date", "invoice_amount"]
      pass

    fields = ["id", "subscription_id", "payment_method", "reference_number", "gateway", "description", \
    "type", "date", "amount", "id_at_gateway", "status", "error_code", "error_text", "voided_at", \
    "void_description", "masked_card_number", "refunded_txn_id", "linked_invoices"]


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/transactions', params, env)

    @staticmethod
    def transactions_for_subscription(id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/transactions' % id, params, env)

    @staticmethod
    def transactions_for_invoice(id, params=None, env=None):
        return request.send('get', '/invoices/%s/transactions' % id, params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/transactions/%s' % id, None, env)

    @staticmethod
    def record_payment(id, params, env=None):
        return request.send('post', '/invoices/%s/record_payment' % id, params, env)

    @staticmethod
    def refund(id, params=None, env=None):
        return request.send('post', '/transactions/%s/refund' % id, params, env)
