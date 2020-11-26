import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class QuotedSubscription(Model):
    class Addon(Model):
      fields = ["id", "quantity", "unit_price", "amount", "trial_end", "remaining_billing_cycles", "quantity_in_decimal", "unit_price_in_decimal", "amount_in_decimal"]
      pass
    class EventBasedAddon(Model):
      fields = ["id", "quantity", "unit_price", "service_period_in_days", "on_event", "charge_once", "quantity_in_decimal", "unit_price_in_decimal"]
      pass
    class Coupon(Model):
      fields = ["coupon_id", "apply_till", "applied_count", "coupon_code"]
      pass
    class SubscriptionItem(Model):
      fields = ["item_price_id", "item_type", "quantity", "unit_price", "amount", "free_quantity", "trial_end", "billing_cycles", "service_period_days", "charge_on_event", "charge_once", "charge_on_option"]
      pass
    class ItemTier(Model):
      fields = ["item_price_id", "starting_unit", "ending_unit", "price"]
      pass

    fields = ["id", "plan_id", "plan_quantity", "plan_unit_price", "setup_fee", "billing_period", \
    "billing_period_unit", "start_date", "trial_end", "remaining_billing_cycles", "po_number", "auto_collection", \
    "addons", "event_based_addons", "coupons", "subscription_items", "item_tiers"]

