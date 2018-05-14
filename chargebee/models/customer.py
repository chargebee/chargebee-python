import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Customer(Model):
    class BillingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class ReferralUrl(Model):
      fields = ["external_customer_id", "referral_sharing_url", "created_at", "updated_at", "referral_campaign_id", "referral_account_id", "referral_external_campaign_id", "referral_system"]
      pass
    class Contact(Model):
      fields = ["id", "first_name", "last_name", "email", "phone", "label", "enabled", "send_account_email", "send_billing_email"]
      pass
    class PaymentMethod(Model):
      fields = ["type", "gateway", "gateway_account_id", "status", "reference_id"]
      pass
    class Balance(Model):
      fields = ["promotional_credits", "excess_payments", "refundable_credits", "unbilled_charges", "currency_code", "balance_currency_code"]
      pass

    fields = ["id", "first_name", "last_name", "email", "phone", "company", "vat_number", "auto_collection", \
    "net_term_days", "allow_direct_debit", "created_at", "created_from_ip", "taxability", "entity_code", \
    "exempt_number", "resource_version", "updated_at", "locale", "consolidated_invoicing", "billing_date", \
    "billing_date_mode", "billing_day_of_week", "billing_day_of_week_mode", "card_status", "fraud_flag", \
    "primary_payment_source_id", "backup_payment_source_id", "billing_address", "referral_urls", \
    "contacts", "payment_method", "invoice_notes", "preferred_currency_code", "promotional_credits", \
    "unbilled_charges", "refundable_credits", "excess_payments", "balances", "meta_data", "deleted", \
    "registered_for_gst"]


    @staticmethod
    def create(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("customers"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id), None, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id), params, env, headers)

    @staticmethod
    def update_payment_method(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"update_payment_method"), params, env, headers)

    @staticmethod
    def update_billing_info(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"update_billing_info"), params, env, headers)

    @staticmethod
    def contacts_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"contacts"), params, env, headers)

    @staticmethod
    def assign_payment_role(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"assign_payment_role"), params, env, headers)

    @staticmethod
    def add_contact(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"add_contact"), params, env, headers)

    @staticmethod
    def update_contact(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"update_contact"), params, env, headers)

    @staticmethod
    def delete_contact(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"delete_contact"), params, env, headers)

    @staticmethod
    def add_promotional_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"add_promotional_credits"), params, env, headers)

    @staticmethod
    def deduct_promotional_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"deduct_promotional_credits"), params, env, headers)

    @staticmethod
    def set_promotional_credits(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"set_promotional_credits"), params, env, headers)

    @staticmethod
    def record_excess_payment(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"record_excess_payment"), params, env, headers)

    @staticmethod
    def collect_payment(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"collect_payment"), params, env, headers)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"delete"), params, env, headers)

    @staticmethod
    def move(params, env=None, headers=None):
        return request.send('post', request.uri_path("customers","move"), params, env, headers)

    @staticmethod
    def change_billing_date(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"change_billing_date"), params, env, headers)
