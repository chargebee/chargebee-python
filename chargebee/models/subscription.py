import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError
import warnings


class Subscription(Model):
    class SubscriptionItem(Model):
      fields = ["item_price_id", "item_type", "quantity", "quantity_in_decimal", "metered_quantity", "last_calculated_at", "unit_price", "unit_price_in_decimal", "amount", "current_term_start", "current_term_end", "next_billing_at", "amount_in_decimal", "billing_period", "billing_period_unit", "free_quantity", "free_quantity_in_decimal", "trial_end", "billing_cycles", "service_period_days", "charge_on_event", "charge_once", "charge_on_option", "proration_type", "usage_accumulation_reset_frequency"]
      pass
    class ItemTier(Model):
      fields = ["item_price_id", "starting_unit", "ending_unit", "price", "starting_unit_in_decimal", "ending_unit_in_decimal", "price_in_decimal", "pricing_type", "package_size", "index"]
      pass
    class ChargedItem(Model):
      fields = ["item_price_id", "last_charged_at"]
      pass
    class Addon(Model):
      fields = ["id", "quantity", "unit_price", "amount", "trial_end", "remaining_billing_cycles", "quantity_in_decimal", "unit_price_in_decimal", "amount_in_decimal", "proration_type"]
      pass
    class EventBasedAddon(Model):
      fields = ["id", "quantity", "unit_price", "service_period_in_days", "on_event", "charge_once", "quantity_in_decimal", "unit_price_in_decimal"]
      pass
    class ChargedEventBasedAddon(Model):
      fields = ["id", "last_charged_at"]
      pass
    class Coupon(Model):
      fields = ["coupon_id", "apply_till", "applied_count", "coupon_code"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class ReferralInfo(Model):
      fields = ["referral_code", "coupon_code", "referrer_id", "external_reference_id", "reward_status", "referral_system", "account_id", "campaign_id", "external_campaign_id", "friend_offer_type", "referrer_reward_type", "notify_referral_system", "destination_url", "post_purchase_widget_enabled"]
      pass
    class BillingOverride(Model):
      fields = ["max_excess_payment_usage", "max_refundable_credits_usage"]
      pass
    class ContractTerm(Model):
      fields = ["id", "status", "contract_start", "contract_end", "billing_cycle", "action_at_term_end", "total_contract_value", "total_contract_value_before_tax", "cancellation_cutoff_period", "created_at", "subscription_id", "remaining_billing_cycles"]
      pass
    class Discount(Model):
      fields = ["id", "invoice_name", "type", "percentage", "amount", "quantity", "currency_code", "duration_type", "period", "period_unit", "included_in_mrr", "apply_on", "item_price_id", "created_at", "apply_till", "applied_count", "coupon_id", "index"]
      pass

    fields = ["id", "currency_code", "plan_id", "plan_quantity", "plan_unit_price", "setup_fee", \
    "billing_period", "billing_period_unit", "start_date", "trial_end", "remaining_billing_cycles", \
    "po_number", "auto_collection", "plan_quantity_in_decimal", "plan_unit_price_in_decimal", "customer_id", \
    "plan_amount", "plan_free_quantity", "status", "trial_start", "trial_end_action", "current_term_start", \
    "current_term_end", "next_billing_at", "created_at", "started_at", "activated_at", "gift_id", \
    "contract_term_billing_cycle_on_renewal", "override_relationship", "pause_date", "resume_date", \
    "cancelled_at", "cancel_reason", "affiliate_token", "created_from_ip", "resource_version", "updated_at", \
    "has_scheduled_advance_invoices", "has_scheduled_changes", "payment_source_id", "plan_free_quantity_in_decimal", \
    "plan_amount_in_decimal", "cancel_schedule_created_at", "offline_payment_method", "channel", \
    "net_term_days", "active_id", "subscription_items", "item_tiers", "charged_items", "due_invoices_count", \
    "due_since", "total_dues", "mrr", "arr", "exchange_rate", "base_currency_code", "addons", "event_based_addons", \
    "charged_event_based_addons", "coupon", "coupons", "shipping_address", "referral_info", "billing_override", \
    "invoice_notes", "meta_data", "deleted", "changes_scheduled_at", "contract_term", "cancel_reason_code", \
    "free_period", "free_period_unit", "create_pending_invoices", "auto_close_invoices", "discounts", \
    "business_entity_id", "metadata" ]
    @property
    def metadata(self):
        warnings.warn(
        "`metadata` please use meta_data instead",
        DeprecationWarning,
        stacklevel=2
        )
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        warnings.warn(
        "`metadata` please use meta_data instead",
        DeprecationWarning,
        stacklevel=2
        )
        self._metadata = value



    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
            "exemption_details": 1,
            "additional_information": 1,
            "billing_address": 1,
        }
        return request.send('post', request.uri_path("subscriptions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_for_customer(id, params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("customers",id,"subscriptions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_with_items(id, params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("customers",id,"subscription_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send_list_request('get', request.uri_path("subscriptions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def subscriptions_for_customer(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"subscriptions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def contract_terms_for_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"contract_terms"), params, env, headers, None, False,json_keys)

    @staticmethod
    def list_discounts(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"discounts"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve_with_scheduled_changes(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"retrieve_with_scheduled_changes"), None, env, headers, None, False,json_keys)

    @staticmethod
    def remove_scheduled_changes(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_changes"), None, env, headers, None, False,json_keys)

    @staticmethod
    def remove_scheduled_cancellation(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_cancellation"), params, env, headers, None, False,json_keys)

    @staticmethod
    def remove_coupons(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"remove_coupons"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("subscriptions",id), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_for_items(id, params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("subscriptions",id,"update_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def change_term_end(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"change_term_end"), params, env, headers, None, False,json_keys)

    @staticmethod
    def reactivate(id, params=None, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("subscriptions",id,"reactivate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def add_charge_at_term_end(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"add_charge_at_term_end"), params, env, headers, None, False,json_keys)

    @staticmethod
    def charge_addon_at_term_end(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"charge_addon_at_term_end"), params, env, headers, None, False,json_keys)

    @staticmethod
    def charge_future_renewals(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"charge_future_renewals"), params, env, headers, None, False,json_keys)

    @staticmethod
    def edit_advance_invoice_schedule(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"edit_advance_invoice_schedule"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve_advance_invoice_schedule(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"retrieve_advance_invoice_schedule"), None, env, headers, None, False,json_keys)

    @staticmethod
    def remove_advance_invoice_schedule(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"remove_advance_invoice_schedule"), params, env, headers, None, False,json_keys)

    @staticmethod
    def regenerate_invoice(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"regenerate_invoice"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_subscription(params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("subscriptions","import_subscription"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_for_customer(id, params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("customers",id,"import_subscription"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_contract_term(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"import_contract_term"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_unbilled_charges(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"import_unbilled_charges"), params, env, headers, None, False,json_keys)

    @staticmethod
    def import_for_items(id, params, env=None, headers=None):
        json_keys = { 
            "meta_data": 0,
        }
        return request.send('post', request.uri_path("customers",id,"import_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def override_billing_profile(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"override_billing_profile"), params, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"delete"), None, env, headers, None, False,json_keys)

    @staticmethod
    def pause(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"pause"), params, env, headers, None, False,json_keys)

    @staticmethod
    def cancel(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"cancel"), params, env, headers, None, False,json_keys)

    @staticmethod
    def cancel_for_items(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"cancel_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def resume(id, params=None, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("subscriptions",id,"resume"), params, env, headers, None, False,json_keys)

    @staticmethod
    def remove_scheduled_pause(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_pause"), None, env, headers, None, False,json_keys)

    @staticmethod
    def remove_scheduled_resumption(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_resumption"), None, env, headers, None, False,json_keys)

    @staticmethod
    def move(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"move"), params, env, headers, None, False,json_keys)
