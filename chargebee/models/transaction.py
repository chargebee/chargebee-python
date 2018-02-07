import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Transaction(Model):
    class LinkedInvoice(Model):
      fields = ["invoice_id", "applied_amount", "applied_at", "invoice_date", "invoice_total", "invoice_status"]
      pass
    class LinkedCreditNote(Model):
      fields = ["cn_id", "applied_amount", "applied_at", "cn_reason_code", "cn_date", "cn_total", "cn_status", "cn_reference_invoice_id"]
      pass
    class LinkedRefund(Model):
      fields = ["txn_id", "txn_status", "txn_date", "txn_amount"]
      pass

    fields = ["id", "customer_id", "subscription_id", "gateway_account_id", "payment_source_id", \
    "payment_method", "reference_number", "gateway", "type", "date", "settled_at", "currency_code", \
    "amount", "id_at_gateway", "status", "fraud_flag", "error_code", "error_text", "voided_at", \
    "resource_version", "updated_at", "fraud_reason", "amount_unused", "masked_card_number", "reference_transaction_id", \
    "refunded_txn_id", "reversal_transaction_id", "linked_invoices", "linked_credit_notes", "linked_refunds", \
    "deleted"]


    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("transactions"), params, env, headers)

    @staticmethod
    def transactions_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"transactions"), params, env, headers)

    @staticmethod
    def transactions_for_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"transactions"), params, env, headers)

    @staticmethod
    def payments_for_invoice(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("invoices",id,"payments"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("transactions",id), None, env, headers)
