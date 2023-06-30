import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentReferenceNumber(Model):

    fields = ["id", "type", "number", "invoice_id"]

