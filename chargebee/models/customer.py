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
      fields = ["promotional_credits", "excess_payments", "refundable_credits", "unbilled_charges", "currency_code", "balance_currency_code", "business_entity_id"]
      pass
    class EntityIdentifier(Model):
      fields = ["id", "value", "scheme", "standard"]
      pass
    class TaxProvidersField(Model):
      fields = ["provider_name", "field_id", "field_value"]
      pass
    class Relationship(Model):
      fields = ["parent_id", "payment_owner_id", "invoice_owner_id"]
      pass
    class ParentAccountAccess(Model):
      fields = ["portal_edit_child_subscriptions", "portal_download_child_invoices", "send_subscription_emails", "send_invoice_emails", "send_payment_emails"]
      pass
    class ChildAccountAccess(Model):
      fields = ["portal_edit_subscriptions", "portal_download_invoices", "send_subscription_emails", "send_invoice_emails", "send_payment_emails"]
      pass

    fields = ["id", "first_name", "last_name", "email", "phone", "company", "vat_number", "auto_collection", \
    "offline_payment_method", "net_term_days", "vat_number_validated_time", "vat_number_status", \
    "allow_direct_debit", "is_location_valid", "created_at", "created_from_ip", "exemption_details", \
    "taxability", "entity_code", "exempt_number", "resource_version", "updated_at", "locale", "billing_date", \
    "billing_month", "billing_date_mode", "billing_day_of_week", "billing_day_of_week_mode", "pii_cleared", \
    "auto_close_invoices", "channel", "active_id", "card_status", "fraud_flag", "primary_payment_source_id", \
    "backup_payment_source_id", "billing_address", "referral_urls", "contacts", "payment_method", \
    "invoice_notes", "business_entity_id", "preferred_currency_code", "promotional_credits", "unbilled_charges", \
    "refundable_credits", "excess_payments", "balances", "entity_identifiers", "tax_providers_fields", \
    "is_einvoice_enabled", "einvoicing_method", "meta_data", "deleted", "registered_for_gst", "consolidated_invoicing", \
    "customer_type", "business_customer_without_vat_number", "client_profile_id", "relationship", \
    "use_default_hierarchy_settings", "parent_account_access", "child_account_access", "vat_number_prefix", \
    "entity_identifier_scheme", "entity_identifier_standard"]


    @staticmethod
    def create(params=None, env=None, headers=None):
        json_keys = { 
            "exemption_details": 0,
            "meta_data": 0,
            "additional_information": 1,
            "billing_address": 1,
        }
        return request.send('post', request.uri_path("customers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("customers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        json_keys = { 
            "exemption_details": 0,
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("customers",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_payment_method(id, params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("customers",id,"update_payment_method"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_billing_info(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"update_billing_info"), params, env, headers, None, False,json_keys)

    @staticmethod
    def contacts_for_customer(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"contacts"), params, env, headers, None, False,json_keys)

    @staticmethod
    def assign_payment_role(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"assign_payment_role"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_contact(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"add_contact"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_contact(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"update_contact"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete_contact(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"delete_contact"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_promotional_credits(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"add_promotional_credits"), params, env, headers, None, False,json_keys)

    @staticmethod
    def deduct_promotional_credits(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"deduct_promotional_credits"), params, env, headers, None, False,json_keys)

    @staticmethod
    def set_promotional_credits(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"set_promotional_credits"), params, env, headers, None, False,json_keys)

    @staticmethod
    def record_excess_payment(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"record_excess_payment"), params, env, headers, None, False,json_keys)

    @staticmethod
    def collect_payment(id, params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("customers",id,"collect_payment"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"delete"), params, env, headers, None, False,json_keys)

    @staticmethod
    def move(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers","move"), params, env, headers, None, False,json_keys)

    @staticmethod
    def change_billing_date(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"change_billing_date"), params, env, headers, None, False,json_keys)

    @staticmethod
    def merge(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers","merge"), params, env, headers, None, False,json_keys)

    @staticmethod
    def clear_personal_data(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"clear_personal_data"), None, env, headers, None, False,json_keys)

    @staticmethod
    def relationships(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"relationships"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete_relationship(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"delete_relationship"), None, env, headers, None, False,json_keys)

    @staticmethod
    def hierarchy(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"hierarchy"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list_hierarchy_detail(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"hierarchy_detail"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_hierarchy_settings(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"update_hierarchy_settings"), params, env, headers, None, False,json_keys)
