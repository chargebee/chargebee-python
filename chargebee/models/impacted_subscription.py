import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ImpactedSubscription(Model):
    class Download(Model):
      fields = ["download_url", "valid_till", "mime_type"]
      pass

    fields = ["count", "download", "subscription_ids"]

