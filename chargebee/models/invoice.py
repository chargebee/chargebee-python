import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Invoice(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", "discount_amount", "item_level_discount_amount", "metered", "is_percentage_pricing", "reference_line_item_id", "description", "entity_description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class LineItemTier(Model):
      fields = ["line_item_id", "starting_unit", "ending_unit", "quantity_used", "unit_amount", "starting_unit_in_decimal", "ending_unit_in_decimal", "quantity_used_in_decimal", "unit_amount_in_decimal", "pricing_type", "package_size"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "entity_id", "discount_amount"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "date_to", "date_from", "prorated_taxable_amount", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LineItemCredit(Model):
      fields = ["cn_id", "applied_amount", "line_item_id"]
      pass
    class LineItemAddress(Model):
      fields = ["line_item_id", "first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "line_item_id", "entity_type", "discount_type", "entity_id", "coupon_set_code"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class TaxOrigin(Model):
      fields = ["country", "registration_number"]
      pass
    class LinkedPayment(Model):
      fields = ["txn_id", "applied_amount", "applied_at", "txn_status", "txn_date", "txn_amount"]
      pass
    class ReferenceTransaction(Model):
      fields = ["applied_amount", "applied_at", "txn_id", "txn_status", "txn_date", "txn_amount", "txn_type", "amount_capturable", "authorization_reason"]
      pass
    class DunningAttempt(Model):
      fields = ["attempt", "transaction_id", "dunning_type", "created_at", "txn_status", "txn_amount", "retry_engine"]
      pass
    class AppliedCredit(Model):
      fields = ["cn_id", "applied_amount", "applied_at", "cn_reason_code", "cn_create_reason_code", "cn_date", "cn_status", "tax_application"]
      pass
    class AdjustmentCreditNote(Model):
      fields = ["cn_id", "cn_reason_code", "cn_create_reason_code", "cn_date", "cn_total", "cn_status"]
      pass
    class IssuedCreditNote(Model):
      fields = ["cn_id", "cn_reason_code", "cn_create_reason_code", "cn_date", "cn_total", "cn_status"]
      pass
    class LinkedOrder(Model):
      fields = ["id", "document_number", "status", "order_type", "reference_id", "fulfillment_status", "batch_id", "created_at"]
      pass
    class Note(Model):
      fields = ["note", "entity_id", "entity_type"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class StatementDescriptor(Model):
      fields = ["id", "descriptor"]
      pass
    class Einvoice(Model):
      fields = ["id", "reference_number", "status", "message"]
      pass
    class SiteDetailsAtCreation(Model):
      fields = ["timezone", "organization_address"]
      pass

    fields = ["id", "customer_id", "payment_owner", "subscription_id", "recurring", "status", \
    "date", "due_date", "net_term_days", "po_number", "vat_number", "price_type", "exchange_rate", \
    "local_currency_exchange_rate", "currency_code", "local_currency_code", "tax", "sub_total", \
    "sub_total_in_local_currency", "total", "total_in_local_currency", "amount_due", "amount_adjusted", \
    "amount_paid", "paid_at", "write_off_amount", "credits_applied", "dunning_status", "next_retry_at", \
    "voided_at", "resource_version", "updated_at", "line_items_next_offset", "first_invoice", "new_sales_amount", \
    "has_advance_charges", "term_finalized", "is_gifted", "generated_at", "expected_payment_date", \
    "amount_to_collect", "round_off_amount", "line_items", "line_item_tiers", "line_item_discounts", \
    "line_item_taxes", "line_item_credits", "line_item_addresses", "discounts", "taxes", "tax_origin", \
    "linked_payments", "reference_transactions", "dunning_attempts", "applied_credits", "adjustment_credit_notes", \
    "issued_credit_notes", "linked_orders", "notes", "shipping_address", "billing_address", "statement_descriptor", \
    "einvoice", "void_reason_code", "deleted", "tax_category", "vat_number_prefix", "channel", "business_entity_id", \
    "site_details_at_creation"]


    @staticmethod
    def create(params=None, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
            "billing_address": 1,
        }
        return request.send('post', request.uri_path("invoices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_for_charge_items_and_charges(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
            "billing_address": 1,
        }
        return request.send('post', request.uri_path("invoices","create_for_charge_items_and_charges"), params, env, headers, None, False,json_keys)

    @staticmethod
    def charge(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices","charge"), params, env, headers, None, False,json_keys)

    @staticmethod
    def charge_addon(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices","charge_addon"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_for_charge_item(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices","create_for_charge_item"), params, env, headers, None, False,json_keys)

    @staticmethod
    def stop_dunning(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"stop_dunning"), params, env, headers, None, False,json_keys)

    @staticmethod
    def pause_dunning(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"pause_dunning"), params, env, headers, None, False,json_keys)

    @staticmethod
    def resume_dunning(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"resume_dunning"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_invoice(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices","import_invoice"), params, env, headers, None, False,json_keys)

    @staticmethod
    def apply_payments(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"apply_payments"), params, env, headers, None, False,json_keys)

    @staticmethod
    def sync_usages(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"sync_usages"), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete_line_items(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"delete_line_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def apply_credits(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"apply_credits"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("invoices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def invoices_for_customer(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"invoices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def invoices_for_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"invoices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("invoices",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def pdf(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"pdf"), params, env, headers, None, False,json_keys)

    @staticmethod
    def download_einvoice(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("invoices",id,"download_einvoice"), None, env, headers, None, False,json_keys)

    @staticmethod
    def list_payment_reference_numbers(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("invoices","payment_reference_numbers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_charge(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"add_charge"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_addon_charge(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"add_addon_charge"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_charge_item(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"add_charge_item"), params, env, headers, None, False,json_keys)

    @staticmethod
    def close(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"close"), params, env, headers, None, False,json_keys)

    @staticmethod
    def collect_payment(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"collect_payment"), params, env, headers, None, False,json_keys)

    @staticmethod
    def record_payment(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"record_payment"), params, env, headers, None, False,json_keys)

    @staticmethod
    def record_tax_withheld(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"record_tax_withheld"), params, env, headers, None, False,json_keys)

    @staticmethod
    def remove_tax_withheld(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"remove_tax_withheld"), params, env, headers, None, False,json_keys)

    @staticmethod
    def refund(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"refund"), params, env, headers, None, False,json_keys)

    @staticmethod
    def record_refund(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"record_refund"), params, env, headers, None, False,json_keys)

    @staticmethod
    def remove_payment(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"remove_payment"), params, env, headers, None, False,json_keys)

    @staticmethod
    def remove_credit_note(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"remove_credit_note"), params, env, headers, None, False,json_keys)

    @staticmethod
    def void_invoice(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"void"), params, env, headers, None, False,json_keys)

    @staticmethod
    def write_off(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"write_off"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"delete"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_details(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"update_details"), params, env, headers, None, False,json_keys)

    @staticmethod
    def apply_payment_schedule_scheme(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"apply_payment_schedule_scheme"), params, env, headers, None, False,json_keys)

    @staticmethod
    def payment_schedules(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("invoices",id,"payment_schedules"), None, env, headers, None, False,json_keys)

    @staticmethod
    def resend_einvoice(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"resend_einvoice"), None, env, headers, None, False,json_keys)

    @staticmethod
    def send_einvoice(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("invoices",id,"send_einvoice"), None, env, headers, None, False,json_keys)
