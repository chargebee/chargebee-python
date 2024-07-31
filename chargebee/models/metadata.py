import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Metadata(Model):

    fields = ["change_type"]

