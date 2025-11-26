import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Einvoice(Model):

    fields = ["id", "reference_number", "status", "message"]

