import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SubscriptionEstimate(Model):

    fields = ["id", "status", "next_billing_at"]

