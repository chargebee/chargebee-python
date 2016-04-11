import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class InvoiceEstimate(Model):
    class LineItem(Model):
      fields = ["date_from", "date_to", "unit_amount", "quantity", "is_taxed", "tax_amount", "tax_rate", "amount", "discount_amount", "item_level_discount_amount", "description", "entity_type", "entity_id"]
      pass
    class Discount(Model):
      fields = ["amount", "description", "entity_type", "entity_id"]
      pass
    class Tax(Model):
      fields = ["amount", "description"]
      pass

    fields = ["recurring", "price_type", "sub_total", "total", "credits_applied", "amount_paid", \
    "amount_due", "line_items", "discounts", "taxes"]

