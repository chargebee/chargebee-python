import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelSubscriptionItemScheduledChange(Model):
    class CurrentState(Model):
      fields = ["item_id_at_source"]
      pass
    class ScheduledState(Model):
      fields = ["item_id_at_source"]
      pass

    fields = ["id", "omnichannel_subscription_item_id", "scheduled_at", "change_type", "created_at", \
    "modified_at", "resource_version", "current_state", "scheduled_state"]

