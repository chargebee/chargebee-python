import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Token(Model):

    fields = ["id", "gateway", "gateway_account_id", "payment_method_type", "status", "id_at_vault", \
    "vault", "ip_address", "resource_version", "updated_at", "created_at", "expired_at"]

