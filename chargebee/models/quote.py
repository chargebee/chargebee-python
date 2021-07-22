import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Quote(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", "discount_amount", "item_level_discount_amount", "description", "entity_description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "entity_id"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "entity_id", "discount_amount"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LineItemTier(Model):
      fields = ["line_item_id", "starting_unit", "ending_unit", "quantity_used", "unit_amount", "starting_unit_in_decimal", "ending_unit_in_decimal", "quantity_used_in_decimal", "unit_amount_in_decimal"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass

    fields = ["id", "name", "po_number", "customer_id", "subscription_id", "invoice_id", "status", \
    "operation_type", "vat_number", "price_type", "valid_till", "date", "total_payable", "charge_on_acceptance", \
    "sub_total", "total", "credits_applied", "amount_paid", "amount_due", "version", "resource_version", \
    "updated_at", "vat_number_prefix", "line_items", "discounts", "line_item_discounts", "taxes", \
    "line_item_taxes", "line_item_tiers", "currency_code", "notes", "shipping_address", "billing_address", \
    "contract_term_start", "contract_term_end", "contract_term_termination_fee"]


    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("quotes",id), None, env, headers)

    @staticmethod
    def create_sub_for_customer_quote(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"create_subscription_quote"), params, env, headers)

    @staticmethod
    def edit_create_sub_for_customer_quote(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"edit_create_subscription_quote"), params, env, headers)

    @staticmethod
    def update_subscription_quote(params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes","update_subscription_quote"), params, env, headers)

    @staticmethod
    def edit_update_subscription_quote(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"edit_update_subscription_quote"), params, env, headers)

    @staticmethod
    def create_for_onetime_charges(params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes","create_for_onetime_charges"), params, env, headers)

    @staticmethod
    def edit_one_time_quote(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"edit_one_time_quote"), params, env, headers)

    @staticmethod
    def create_sub_items_for_customer_quote(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"create_subscription_quote_for_items"), params, env, headers)

    @staticmethod
    def edit_create_sub_customer_quote_for_items(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"edit_create_subscription_quote_for_items"), params, env, headers)

    @staticmethod
    def update_subscription_quote_for_items(params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes","update_subscription_quote_for_items"), params, env, headers)

    @staticmethod
    def edit_update_subscription_quote_for_items(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"edit_update_subscription_quote_for_items"), params, env, headers)

    @staticmethod
    def create_for_charge_items_and_charges(params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes","create_for_charge_items_and_charges"), params, env, headers)

    @staticmethod
    def edit_for_charge_items_and_charges(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"edit_for_charge_items_and_charges"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("quotes"), params, env, headers)

    @staticmethod
    def quote_line_groups_for_quote(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("quotes",id,"quote_line_groups"), params, env, headers)

    @staticmethod
    def convert(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"convert"), params, env, headers)

    @staticmethod
    def update_status(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"update_status"), params, env, headers)

    @staticmethod
    def extend_expiry_date(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"extend_expiry_date"), params, env, headers)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"delete"), params, env, headers)

    @staticmethod
    def pdf(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("quotes",id,"pdf"), params, env, headers)
