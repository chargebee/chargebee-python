import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Card(Model):

    fields = ["customer_id", "status", "gateway", "first_name", "last_name", "iin", "last4", \
    "card_type", "expiry_month", "expiry_year", "billing_addr1", "billing_addr2", "billing_city", \
    "billing_state", "billing_country", "billing_zip", "masked_number"]


    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', request.uri_path("cards",id), None, env)

    @staticmethod
    def update_card_for_customer(id, params, env=None):
        return request.send('post', request.uri_path("customers",id,"credit_card"), params, env)

    @staticmethod
    def delete_card_for_customer(id, env=None):
        return request.send('post', request.uri_path("customers",id,"delete_card"), None, env)
