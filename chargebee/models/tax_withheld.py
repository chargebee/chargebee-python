import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class TaxWithheld(Model):

    fields = ["id", "user", "reference_number", "description", "type", "payment_method", "date", \
    "currency_code", "amount", "resource_version", "updated_at", "exchange_rate"]

