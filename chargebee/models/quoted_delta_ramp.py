import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class QuotedDeltaRamp(Model):
    class LineItem(Model):
      fields = ["item_level_discount_per_billing_cycle_in_decimal"]
      pass

    fields = ["line_items"]

