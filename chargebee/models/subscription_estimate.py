import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class SubscriptionEstimate(Model):
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class ContractTerm(Model):
      fields = ["id", "status", "contract_start", "contract_end", "billing_cycle", "action_at_term_end", "total_contract_value", "cancellation_cutoff_period", "created_at", "subscription_id", "remaining_billing_cycles"]
      pass

    fields = ["id", "currency_code", "status", "trial_end_action", "next_billing_at", "pause_date", \
    "resume_date", "shipping_address", "contract_term"]

