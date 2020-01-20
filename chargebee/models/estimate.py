import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

from chargebee.models.credit_note_estimate import CreditNoteEstimate
from chargebee.models.invoice_estimate import InvoiceEstimate
from chargebee.models.subscription_estimate import SubscriptionEstimate
from chargebee.models.unbilled_charge import UnbilledCharge


class Estimate(Model):

    fields = ["created_at", "subscription_estimate", "invoice_estimate", "invoice_estimates", \
    "next_invoice_estimate", "credit_note_estimates", "unbilled_charge_estimates"]

    dependant_types = {
        'subscription_estimate': SubscriptionEstimate,
        'invoice_estimate': InvoiceEstimate,
        'next_invoice_estimate': InvoiceEstimate,
        'invoice_estimates': (InvoiceEstimate,),
        'credit_note_estimates': (CreditNoteEstimate,),
        'unbilled_charge_estimates': (UnbilledCharge,),
    }


    @staticmethod
    def create_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("estimates","create_subscription"), params, env, headers)

    @staticmethod
    def create_sub_for_customer_estimate(id, params, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"create_subscription_estimate"), params, env, headers)

    @staticmethod
    def update_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("estimates","update_subscription"), params, env, headers)

    @staticmethod
    def renewal_estimate(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"renewal_estimate"), params, env, headers)

    @staticmethod
    def upcoming_invoices_estimate(id, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"upcoming_invoices_estimate"), None, env, headers)

    @staticmethod
    def change_term_end(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"change_term_end_estimate"), params, env, headers)

    @staticmethod
    def cancel_subscription(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"cancel_subscription_estimate"), params, env, headers)

    @staticmethod
    def pause_subscription(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"pause_subscription_estimate"), params, env, headers)

    @staticmethod
    def resume_subscription(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"resume_subscription_estimate"), params, env, headers)

    @staticmethod
    def gift_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("estimates","gift_subscription"), params, env, headers)

    @staticmethod
    def create_invoice(params, env=None, headers=None):
        return request.send('post', request.uri_path("estimates","create_invoice"), params, env, headers)
