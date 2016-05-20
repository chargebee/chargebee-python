import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Invoice(Model):
    class LineItem(Model):
      fields = ["id", "date_from", "date_to", "unit_amount", "quantity", "is_taxed", "tax_amount", "tax_rate", "amount", "discount_amount", "item_level_discount_amount", "description", "entity_type", "entity_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "entity_id"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code"]
      pass
    class LinkedPayment(Model):
      fields = ["txn_id", "applied_amount", "applied_at", "txn_status", "txn_date", "txn_amount"]
      pass
    class AppliedCredit(Model):
      fields = ["cn_id", "applied_amount", "applied_at", "cn_reason_code", "cn_date", "cn_status"]
      pass
    class AdjustmentCreditNote(Model):
      fields = ["cn_id", "cn_reason_code", "cn_date", "cn_total", "cn_status"]
      pass
    class IssuedCreditNote(Model):
      fields = ["cn_id", "cn_reason_code", "cn_date", "cn_total", "cn_status"]
      pass
    class LinkedOrder(Model):
      fields = ["id", "status", "reference_id", "fulfillment_status", "batch_id", "created_at"]
      pass
    class Note(Model):
      fields = ["entity_type", "note", "entity_id"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip"]
      pass
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip"]
      pass

    fields = ["id", "po_number", "customer_id", "subscription_id", "recurring", "status", "vat_number", \
    "price_type", "date", "total", "amount_paid", "amount_adjusted", "write_off_amount", "credits_applied", \
    "amount_due", "paid_at", "dunning_status", "next_retry_at", "sub_total", "tax", "first_invoice", \
    "currency_code", "line_items", "discounts", "taxes", "line_item_taxes", "linked_payments", "applied_credits", \
    "adjustment_credit_notes", "issued_credit_notes", "linked_orders", "notes", "shipping_address", \
    "billing_address"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices"), params, env, headers)

    @staticmethod
    def charge(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","charge"), params, env, headers)

    @staticmethod
    def charge_addon(params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices","charge_addon"), params, env, headers)

    @staticmethod
    def stop_dunning(id, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"stop_dunning"), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("invoices"), params, env, headers)

    @staticmethod
    def invoices_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"invoices"), params, env, headers)

    @staticmethod
    def invoices_for_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"invoices"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("invoices",id), None, env, headers)

    @staticmethod
    def pdf(id, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"pdf"), None, env, headers)

    @staticmethod
    def add_charge(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"add_charge"), params, env, headers)

    @staticmethod
    def add_addon_charge(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"add_addon_charge"), params, env, headers)

    @staticmethod
    def close(id, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"close"), None, env, headers)

    @staticmethod
    def collect_payment(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"collect_payment"), params, env, headers)

    @staticmethod
    def record_payment(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"record_payment"), params, env, headers)

    @staticmethod
    def refund(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"refund"), params, env, headers)

    @staticmethod
    def record_refund(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"record_refund"), params, env, headers)

    @staticmethod
    def void_invoice(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"void"), params, env, headers)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("invoices",id,"delete"), params, env, headers)
