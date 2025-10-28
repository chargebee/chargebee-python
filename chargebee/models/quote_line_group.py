import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class QuoteLineGroup(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "unit_amount_in_decimal", "quantity_in_decimal", "amount_in_decimal", "discount_amount", "item_level_discount_amount", "metered", "is_percentage_pricing", "reference_line_item_id", "description", "entity_description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "entity_id", "discount_amount"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "date_to", "date_from", "prorated_taxable_amount", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "line_item_id", "entity_type", "discount_type", "entity_id", "coupon_set_code"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass

    fields = ["version", "id", "sub_total", "total", "credits_applied", "amount_paid", "amount_due", \
    "charge_event", "billing_cycle_number", "line_items", "line_item_discounts", "line_item_taxes", \
    "discounts", "taxes"]

