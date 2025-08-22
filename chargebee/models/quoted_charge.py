import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class QuotedCharge(Model):
    class Charge(Model):
      fields = ["amount", "amount_in_decimal", "description", "service_period_in_days", "avalara_sale_type", "avalara_transaction_type", "avalara_service_type"]
      pass
    class Addon(Model):
      fields = ["id", "quantity", "unit_price", "quantity_in_decimal", "unit_price_in_decimal", "proration_type", "service_period"]
      pass
    class InvoiceItem(Model):
      fields = ["item_price_id", "quantity", "quantity_in_decimal", "unit_price", "unit_price_in_decimal", "service_period_days"]
      pass
    class ItemTier(Model):
      fields = ["item_price_id", "starting_unit", "ending_unit", "price", "starting_unit_in_decimal", "ending_unit_in_decimal", "price_in_decimal", "pricing_type", "package_size", "index"]
      pass
    class Coupon(Model):
      fields = ["coupon_id"]
      pass
    class CouponApplicabilityMapping(Model):
      fields = ["coupon_id", "applicable_item_price_ids"]
      pass

    fields = ["charges", "addons", "invoice_items", "item_tiers", "coupons", "coupon_applicability_mappings"]

