import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class OmnichannelSubscriptionItemOffer(Model):

    fields = ["id", "offer_id_at_source", "category", "category_at_source", "type", "type_at_source", \
    "discount_type", "duration", "percentage", "price_currency", "price_units", "price_nanos", "offer_term_start", \
    "offer_term_end", "resource_version"]

