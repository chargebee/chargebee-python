import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class BusinessEntityTransfer(Model):

    fields = ["id", "resource_type", "resource_id", "active_resource_id", "destination_business_entity_id", \
    "source_business_entity_id", "reason_code", "created_at"]

