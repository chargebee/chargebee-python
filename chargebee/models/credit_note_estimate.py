import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class CreditNoteEstimate(Model):
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

    fields = ["reference_invoice_id", "type", "price_type", "sub_total", "total", "amount_allocated", \
    "amount_available", "line_items", "discounts", "taxes", "line_item_taxes"]

