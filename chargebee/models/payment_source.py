import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentSource(Model):
    class Card(Model):
      fields = ["first_name", "last_name", "iin", "last4", "brand", "funding_type", "expiry_month", "expiry_year", "billing_addr1", "billing_addr2", "billing_city", "billing_state_code", "billing_state", "billing_country", "billing_zip", "masked_number"]
      pass
    class BankAccount(Model):
      fields = ["name_on_account", "bank_name", "mandate_id", "account_type"]
      pass
    class AmazonPayment(Model):
      fields = ["email", "agreement_id"]
      pass
    class Paypal(Model):
      fields = ["email", "agreement_id"]
      pass

    fields = ["id", "customer_id", "type", "reference_id", "status", "gateway", "gateway_account_id", \
    "ip_address", "issuing_country", "card", "bank_account", "amazon_payment", "paypal", "deleted"]


    @staticmethod
    def create_using_temp_token(params, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources","create_using_temp_token"), params, env, headers)

    @staticmethod
    def create_using_permanent_token(params, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources","create_using_permanent_token"), params, env, headers)

    @staticmethod
    def create_card(params, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources","create_card"), params, env, headers)

    @staticmethod
    def update_card(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources",id,"update_card"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("payment_sources",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("payment_sources"), params, env, headers)

    @staticmethod
    def switch_gateway_account(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources",id,"switch_gateway_account"), params, env, headers)

    @staticmethod
    def export_payment_source(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources",id,"export_payment_source"), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("payment_sources",id,"delete"), None, env, headers)
