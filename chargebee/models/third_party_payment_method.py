import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class ThirdPartyPaymentMethod(Model):

    fields = ["type", "gateway", "gateway_account_id", "reference_id"]

