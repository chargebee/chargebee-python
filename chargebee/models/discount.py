import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Discount(Model):

    fields = ["id", "invoice_name", "type", "percentage", "amount", "quantity", "currency_code", \
    "duration_type", "period", "period_unit", "included_in_mrr", "apply_on", "item_price_id", "created_at", \
    "apply_till", "applied_count", "coupon_id", "index"]

