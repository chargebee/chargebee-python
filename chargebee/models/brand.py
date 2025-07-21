import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Brand(Model):

    fields = ["id", "name"]

