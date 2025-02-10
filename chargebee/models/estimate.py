import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Estimate(Model):

    fields = ["created_at", "subscription_estimate", "subscription_estimates", "invoice_estimate", \
    "invoice_estimates", "payment_schedule_estimates", "next_invoice_estimate", "credit_note_estimates", \
    "unbilled_charge_estimates"]


    @staticmethod
    def create_subscription(params, env=None, headers=None):
        json_keys = { 
            "exemption_details": 1,
        }
        return request.send('post', request.uri_path("estimates","create_subscription"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_sub_item_estimate(params, env=None, headers=None):
        json_keys = { 
            "exemption_details": 1,
        }
        return request.send('post', request.uri_path("estimates","create_subscription_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_sub_for_customer_estimate(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"create_subscription_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_sub_item_for_customer_estimate(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("customers",id,"create_subscription_for_items_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_subscription(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("estimates","update_subscription"), params, env, headers, None, False,json_keys)

    @staticmethod
    def update_subscription_for_items(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("estimates","update_subscription_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def renewal_estimate(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("subscriptions",id,"renewal_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def advance_invoice_estimate(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"advance_invoice_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def regenerate_invoice_estimate(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"regenerate_invoice_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def upcoming_invoices_estimate(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("customers",id,"upcoming_invoices_estimate"), None, env, headers, None, False,json_keys)

    @staticmethod
    def change_term_end(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"change_term_end_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def cancel_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"cancel_subscription_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def cancel_subscription_for_items(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"cancel_subscription_for_items_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def pause_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"pause_subscription_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def resume_subscription(id, params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("subscriptions",id,"resume_subscription_estimate"), params, env, headers, None, False,json_keys)

    @staticmethod
    def gift_subscription(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("estimates","gift_subscription"), params, env, headers, None, False,json_keys)

    @staticmethod
    def gift_subscription_for_items(params, env=None, headers=None):
        json_keys = { 
            "additional_information": 1,
        }
        return request.send('post', request.uri_path("estimates","gift_subscription_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_invoice(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("estimates","create_invoice"), params, env, headers, None, False,json_keys)

    @staticmethod
    def create_invoice_for_items(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("estimates","create_invoice_for_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def payment_schedules(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("estimates","payment_schedules"), params, env, headers, None, False,json_keys)
