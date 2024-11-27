import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelTransaction(Model):

    fields = ["id", "id_at_source", "app_id", "price_currency", "price_units", "price_nanos", \
    "type", "transacted_at", "created_at", "resource_version"]

