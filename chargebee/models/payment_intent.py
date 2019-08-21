import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentIntent(Model):
    class PaymentAttempt(Model):
      fields = ["id", "status", "id_at_gateway", "error_code", "error_text", "created_at", "modified_at"]
      pass

    fields = ["id", "status", "amount", "gateway_account_id", "expires_at", "reference_id", \
    "created_at", "modified_at", "customer_id", "gateway", "active_payment_attempt"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("payment_intents"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("payment_intents",id), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("payment_intents",id), None, env, headers)
