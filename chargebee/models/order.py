import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Order(Model):
    class OrderLineItem(Model):
      fields = ["id", "invoice_id", "invoice_line_item_id", "unit_price", "description", "amount", "fulfillment_quantity", "fulfillment_amount", "tax_amount", "amount_paid", "amount_adjusted", "refundable_credits_issued", "refundable_credits", "is_shippable", "sku", "status", "entity_type", "item_level_discount_amount", "discount_amount", "entity_id"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "discount_amount"]
      pass
    class LinkedCreditNote(Model):
      fields = ["amount", "type", "id", "status", "amount_adjusted", "amount_refunded"]
      pass

    fields = ["id", "document_number", "invoice_id", "subscription_id", "customer_id", "status", \
    "cancellation_reason", "payment_status", "order_type", "price_type", "reference_id", "fulfillment_status", \
    "order_date", "shipping_date", "note", "tracking_id", "batch_id", "created_by", "shipment_carrier", \
    "invoice_round_off_amount", "tax", "amount_paid", "amount_adjusted", "refundable_credits_issued", \
    "refundable_credits", "rounding_adjustement", "paid_on", "shipping_cut_off_date", "created_at", \
    "status_update_at", "delivered_at", "shipped_at", "resource_version", "updated_at", "cancelled_at", \
    "order_line_items", "shipping_address", "billing_address", "discount", "sub_total", "total", \
    "line_item_taxes", "line_item_discounts", "linked_credit_notes", "deleted", "currency_code", \
    "is_gifted", "gift_note", "gift_id"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("orders"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("orders",id), params, env, headers)

    @staticmethod
    def assign_order_number(id, env=None, headers=None):
        return request.send('post', request.uri_path("orders",id,"assign_order_number"), None, env, headers)

    @staticmethod
    def cancel(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("orders",id,"cancel"), params, env, headers)

    @staticmethod
    def create_refundable_credit_note(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("orders",id,"create_refundable_credit_note"), params, env, headers)

    @staticmethod
    def reopen(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("orders",id,"reopen"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("orders",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("orders"), params, env, headers)

    @staticmethod
    def orders_for_invoice(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("invoices",id,"orders"), params, env, headers)
