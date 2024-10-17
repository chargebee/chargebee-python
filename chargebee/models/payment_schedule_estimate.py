import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentScheduleEstimate(Model):
    class ScheduleEntry(Model):
      fields = ["id", "date", "amount", "status"]
      pass

    fields = ["id", "scheme_id", "entity_type", "entity_id", "amount", "currency_code", "schedule_entries"]

