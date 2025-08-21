import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SubscriptionEntitlementsUpdatedDetail(Model):

    fields = ["subscription_id", "has_next"]

