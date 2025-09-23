import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelTransaction(Model):
    class LinkedOmnichannelSubscription(Model):
      fields = ["omnichannel_subscription_id"]
      pass
    class LinkedOmnichannelOneTimeOrder(Model):
      fields = ["omnichannel_one_time_order_id"]
      pass

    fields = ["id", "id_at_source", "app_id", "price_currency", "price_units", "price_nanos", \
    "type", "transacted_at", "created_at", "resource_version", "linked_omnichannel_subscriptions", \
    "linked_omnichannel_one_time_orders"]

