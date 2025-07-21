import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class BillingConfiguration(Model):
    class BillingDate(Model):
      fields = ["start_date", "end_date"]
      pass

    fields = ["is_calendar_billing_enabled", "billing_dates"]

