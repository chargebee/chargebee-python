import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentSchedule(Model):
    class ScheduleEntry(Model):
      fields = ["id", "date", "amount", "status"]
      pass

    fields = ["id", "scheme_id", "entity_type", "entity_id", "amount", "created_at", "resource_version", \
    "updated_at", "currency_code", "schedule_entries"]

