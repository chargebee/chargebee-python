import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Contact(Model):

    fields = ["id", "first_name", "last_name", "email", "phone", "label", "enabled", "send_account_email", \
    "send_billing_email"]

