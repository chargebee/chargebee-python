import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentVoucher(Model):
    class LinkedInvoice(Model):
      fields = ["invoice_id", "txn_id", "applied_at"]
      pass

    fields = ["id", "id_at_gateway", "payment_voucher_type", "expires_at", "status", "subscription_id", \
    "currency_code", "amount", "gateway_account_id", "payment_source_id", "gateway", "payload", \
    "error_code", "error_text", "url", "date", "resource_version", "updated_at", "customer_id", \
    "linked_invoices"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_vouchers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("payment_vouchers",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def payment_vouchers_for_invoice(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("invoices",id,"payment_vouchers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def payment_vouchers_for_customer(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"payment_vouchers"), params, env, headers, None, False,json_keys)
