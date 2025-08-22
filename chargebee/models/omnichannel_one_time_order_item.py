import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelOneTimeOrderItem(Model):

    fields = ["id", "item_id_at_source", "item_type_at_source", "quantity", "cancelled_at", \
    "cancellation_reason", "created_at", "resource_version"]

