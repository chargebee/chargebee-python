from chargebee.main import ChargeBee
from chargebee.api_error import APIError


def configure(api_key, site):
    ChargeBee.configure({
        'api_key': api_key,
        'site': site,
    })
