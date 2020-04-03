import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ContractTerm(Model):

    fields = ["id", "status", "contract_start", "contract_end", "billing_cycle", "action_at_term_end", \
    "total_contract_value", "cancellation_cutoff_period", "created_at", "subscription_id", "remaining_billing_cycles"]

