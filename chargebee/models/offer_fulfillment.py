import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OfferFulfillment(Model):
    class Error(Model):
      fields = ["code", "message"]
      pass

    fields = ["id", "personalized_offer_id", "option_id", "processing_type", "status", "redirect_url", \
    "failed_at", "created_at", "completed_at", "error"]


    @staticmethod
    def offer_fulfillments(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("offer_fulfillments"), params, env, headers, "grow", True,json_keys)

    @staticmethod
    def offer_fulfillments_get(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("offer_fulfillments",id), None, env, headers, "grow", True,json_keys)

    @staticmethod
    def offer_fulfillments_update(id, params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("offer_fulfillments",id), params, env, headers, "grow", True,json_keys)
