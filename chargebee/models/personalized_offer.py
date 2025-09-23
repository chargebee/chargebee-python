import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PersonalizedOffer(Model):
    class Content(Model):
      fields = ["title", "description"]
      pass
    class Option(Model):
      fields = ["id", "label", "processing_type", "processing_layout", "redirect_url"]
      pass

    fields = ["id", "offer_id", "content", "options"]


    @staticmethod
    def personalized_offers(params, env=None, headers=None):
        json_keys = { 
            "custom": 0,
        }
        return request.send('post', request.uri_path("personalized_offers"), params, env, headers, "grow", True,json_keys)
