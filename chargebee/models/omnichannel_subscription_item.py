import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelSubscriptionItem(Model):

    fields = ["id", "item_id_at_source", "status", "current_term_start", "current_term_end", \
    "expired_at", "expiration_reason", "cancelled_at", "cancellation_reason", "grace_period_expires_at", \
    "resource_version"]

