import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class TaxWithheld(Model):

    fields = ["id", "reference_number", "description", "date", "currency_code", "amount"]

