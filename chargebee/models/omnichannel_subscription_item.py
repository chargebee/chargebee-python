import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelSubscriptionItem(Model):
    class UpcomingRenewal(Model):
      fields = ["price_currency", "price_units", "price_nanos"]
      pass

    fields = ["id", "item_id_at_source", "item_parent_id_at_source", "status", "auto_renew_status", \
    "current_term_start", "current_term_end", "expired_at", "expiration_reason", "cancelled_at", \
    "cancellation_reason", "grace_period_expires_at", "has_scheduled_changes", "resource_version", \
    "upcoming_renewal"]


    @staticmethod
    def list_omni_sub_item_schedule_changes(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("omnichannel_subscription_items",id,"scheduled_changes"), params, env, headers, None, False,json_keys)
