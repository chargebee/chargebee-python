import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Hierarchy(Model):

    fields = ["customer_id", "parent_id", "payment_owner_id", "invoice_owner_id", "has_children", \
    "children_ids"]

