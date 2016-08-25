import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SubscriptionEstimate(Model):
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass

    fields = ["id", "currency_code", "status", "next_billing_at", "shipping_address"]

