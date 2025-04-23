import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class InvoiceEstimate(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", "discount_amount", "item_level_discount_amount", "metered", "percentage", "reference_line_item_id", "description", "entity_description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "discount_type", "entity_id", "coupon_set_code"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "date_to", "date_from", "prorated_taxable_amount", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LineItemTier(Model):
      fields = ["line_item_id", "starting_unit", "ending_unit", "quantity_used", "unit_amount", "starting_unit_in_decimal", "ending_unit_in_decimal", "quantity_used_in_decimal", "unit_amount_in_decimal", "pricing_type", "package_size"]
      pass
    class LineItemCredit(Model):
      fields = ["cn_id", "applied_amount", "line_item_id"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "entity_id", "discount_amount"]
      pass
    class LineItemAddress(Model):
      fields = ["line_item_id", "first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass

    fields = ["recurring", "price_type", "currency_code", "sub_total", "total", "credits_applied", \
    "amount_paid", "amount_due", "line_items", "discounts", "taxes", "line_item_taxes", "line_item_tiers", \
    "line_item_credits", "line_item_discounts", "round_off_amount", "customer_id", "line_item_addresses"]

