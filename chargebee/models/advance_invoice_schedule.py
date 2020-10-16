import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class AdvanceInvoiceSchedule(Model):
    class FixedIntervalSchedule(Model):
      fields = ["end_schedule_on", "number_of_occurrences", "days_before_renewal", "end_date", "created_at", "terms_to_charge"]
      pass
    class SpecificDatesSchedule(Model):
      fields = ["terms_to_charge", "date", "created_at"]
      pass

    fields = ["id", "schedule_type", "fixed_interval_schedule", "specific_dates_schedule"]

