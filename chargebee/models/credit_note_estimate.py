import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CreditNoteEstimate(Model):
    class LineItem(Model):
      fields = ["id", "subscription_id", "date_from", "date_to", "unit_amount", "quantity", "amount", "pricing_model", "is_taxed", "tax_amount", "tax_rate", "discount_amount", "item_level_discount_amount", "description", "entity_type", "tax_exempt_reason", "entity_id", "customer_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "entity_id"]
      pass
    class Tax(Model):
      fields = ["name", "amount", "description"]
      pass
    class LineItemTax(Model):
      fields = ["line_item_id", "tax_name", "tax_rate", "is_partial_tax_applied", "is_non_compliance_tax", "taxable_amount", "tax_amount", "tax_juris_type", "tax_juris_name", "tax_juris_code", "tax_amount_in_local_currency", "local_currency_code"]
      pass
    class LineItemDiscount(Model):
      fields = ["line_item_id", "discount_type", "coupon_id", "discount_amount"]
      pass
    class LineItemTier(Model):
      fields = ["line_item_id", "starting_unit", "ending_unit", "quantity_used", "unit_amount"]
      pass

    fields = ["reference_invoice_id", "type", "price_type", "currency_code", "sub_total", "total", \
    "amount_allocated", "amount_available", "line_items", "discounts", "taxes", "line_item_taxes", \
    "line_item_discounts", "line_item_tiers", "round_off_amount", "customer_id"]

