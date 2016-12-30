import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CreditNote(Model):
    class LineItem(Model):
      fields = ["id", "date_from", "date_to", "unit_amount", "quantity", "is_taxed", "tax_amount", "tax_rate", "amount", "discount_amount", "item_level_discount_amount", "description", "entity_type", "tax_exempt_reason", "entity_id"]
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
    class LinkedRefund(Model):
      fields = ["txn_id", "applied_amount", "applied_at", "txn_status", "txn_date", "txn_amount"]
      pass
    class Allocation(Model):
      fields = ["invoice_id", "allocated_amount", "allocated_at", "invoice_date", "invoice_status"]
      pass

    fields = ["id", "customer_id", "subscription_id", "reference_invoice_id", "type", "reason_code", \
    "status", "vat_number", "date", "price_type", "currency_code", "total", "amount_allocated", \
    "amount_refunded", "amount_available", "refunded_at", "voided_at", "resource_version", "updated_at", \
    "sub_total", "line_items", "discounts", "taxes", "line_item_taxes", "linked_refunds", "allocations", \
    "deleted"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("credit_notes",id), None, env, headers)

    @staticmethod
    def pdf(id, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes",id,"pdf"), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("credit_notes"), params, env, headers)

    @staticmethod
    def credit_notes_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"credit_notes"), params, env, headers)
