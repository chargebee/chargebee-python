import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class GatewayErrorDetail(Model):

    fields = ["request_id", "error_category", "error_code", "error_message", "decline_code", \
    "decline_message", "network_error_code", "network_error_message", "error_field", "recommendation_code", \
    "recommendation_message", "processor_error_code", "processor_error_message", "error_cause_id", \
    "processor_advice_code"]

