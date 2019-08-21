import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Hierarchy(Model):

    fields = ["parent_id", "payment_owner_id", "invoice_owner_id", "customer_id", "children_ids"]

