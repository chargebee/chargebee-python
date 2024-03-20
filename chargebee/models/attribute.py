import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Attribute(Model):

    fields = ["name", "value"]

