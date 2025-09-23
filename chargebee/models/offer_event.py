import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OfferEvent(Model):



    @staticmethod
    def offer_events(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("offer_events"), params, env, headers, "grow", True,json_keys)
