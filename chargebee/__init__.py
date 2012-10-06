from chargebee.api_error import APIError
from chargebee.models import *
from chargebee.main import ChargeBee


def configure(api_key, site):
    ChargeBee.configure({
        'api_key': api_key,
        'site': site,
    })
