import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SubscriptionEntitlementsCreatedDetail(Model):

    fields = ["subscription_id", "has_next"]

