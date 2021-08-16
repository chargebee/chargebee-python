import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CreditNote(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", "discount_amount", "item_level_discount_amount", "description", "entity_description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "entity_id"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "entity_id", "discount_amount"]
      pass
    class LineItemTier(Model):
      fields = ["line_item_id", "starting_unit", "ending_unit", "quantity_used", "unit_amount", "starting_unit_in_decimal", "ending_unit_in_decimal", "quantity_used_in_decimal", "unit_amount_in_decimal"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LinkedRefund(Model):
      fields = ["txn_id", "applied_amount", "applied_at", "txn_status", "txn_date", "txn_amount", "refund_reason_code"]
      pass
    class Allocation(Model):
      fields = ["invoice_id", "allocated_amount", "allocated_at", "invoice_date", "invoice_status"]
      pass

    fields = ["id", "customer_id", "subscription_id", "reference_invoice_id", "type", "reason_code", \
    "status", "vat_number", "date", "price_type", "currency_code", "total", "amount_allocated", \
    "amount_refunded", "amount_available", "refunded_at", "voided_at", "generated_at", "resource_version", \
    "updated_at", "sub_total", "sub_total_in_local_currency", "total_in_local_currency", "local_currency_code", \
    "round_off_amount", "fractional_correction", "line_items", "discounts", "line_item_discounts", \
    "line_item_tiers", "taxes", "line_item_taxes", "linked_refunds", "allocations", "deleted", "create_reason_code", \
    "vat_number_prefix"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("credit_notes",id), None, env, headers)

    @staticmethod
    def pdf(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes",id,"pdf"), params, env, headers)

    @staticmethod
    def refund(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes",id,"refund"), params, env, headers)

    @staticmethod
    def record_refund(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes",id,"record_refund"), params, env, headers)

    @staticmethod
    def void_credit_note(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes",id,"void"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("credit_notes"), params, env, headers)

    @staticmethod
    def credit_notes_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"credit_notes"), params, env, headers)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("credit_notes",id,"delete"), params, env, headers)
