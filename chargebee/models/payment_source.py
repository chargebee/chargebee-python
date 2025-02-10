import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentSource(Model):
    class Card(Model):
      fields = ["first_name", "last_name", "iin", "last4", "brand", "funding_type", "expiry_month", "expiry_year", "billing_addr1", "billing_addr2", "billing_city", "billing_state_code", "billing_state", "billing_country", "billing_zip", "masked_number"]
      pass
    class BankAccount(Model):
      fields = ["last4", "name_on_account", "first_name", "last_name", "direct_debit_scheme", "bank_name", "mandate_id", "account_type", "echeck_type", "account_holder_type", "email"]
      pass
    class CustVoucherSource(Model):
      fields = ["last4", "first_name", "last_name", "email"]
      pass
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class AmazonPayment(Model):
      fields = ["email", "agreement_id"]
      pass
    class Upi(Model):
      fields = ["vpa"]
      pass
    class Paypal(Model):
      fields = ["email", "agreement_id"]
      pass
    class Venmo(Model):
      fields = ["user_name"]
      pass
    class KlarnaPayNow(Model):
      fields = ["email"]
      pass
    class Mandate(Model):
      fields = ["id", "subscription_id", "created_at"]
      pass

    fields = ["id", "resource_version", "updated_at", "created_at", "customer_id", "type", \
    "reference_id", "status", "gateway", "gateway_account_id", "ip_address", "issuing_country", \
    "card", "bank_account", "boleto", "billing_address", "amazon_payment", "upi", "paypal", "venmo", \
    "klarna_pay_now", "mandates", "deleted", "business_entity_id"]


    @staticmethod
    def create_using_temp_token(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 0,
        }
        return request.send('post', request.uri_path("payment_sources","create_using_temp_token"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_using_permanent_token(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 0,
        }
        return request.send('post', request.uri_path("payment_sources","create_using_permanent_token"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_using_token(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources","create_using_token"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_using_payment_intent(params, env=None, headers=None):
        json_keys = { 
            "additional_info": 1,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("payment_sources","create_using_payment_intent"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_voucher_payment_source(params, env=None, headers=None):
        json_keys = { 
            "billing_address": 1,
        }
        return request.send('post', request.uri_path("payment_sources","create_voucher_payment_source"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_card(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("payment_sources","create_card"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_bank_account(params, env=None, headers=None):
        json_keys = { 
            "billing_address": 1,
        }
        return request.send('post', request.uri_path("payment_sources","create_bank_account"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_card(id, params=None, env=None, headers=None):
        json_keys = { 
            "gateway_meta_data": 0,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("payment_sources",id,"update_card"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_bank_account(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources",id,"update_bank_account"), params, env, headers, None, False,json_keys)

    @staticmethod
    def verify_bank_account(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources",id,"verify_bank_account"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("payment_sources",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("payment_sources"), params, env, headers, None, False,json_keys)

    @staticmethod
    def switch_gateway_account(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources",id,"switch_gateway_account"), params, env, headers, None, False,json_keys)

    @staticmethod
    def export_payment_source(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources",id,"export_payment_source"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete_local(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_sources",id,"delete_local"), None, env, headers, None, False,json_keys)
