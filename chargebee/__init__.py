from chargebee.api_error import APIError,PaymentError,InvalidRequestError,OperationFailedError
from chargebee.models import *
from chargebee.main import ChargeBee


def configure(api_key, site):
    ChargeBee.configure({
        'api_key': api_key,
        'site': site,
    })

def update_connect_timeout_secs(connect_timeout):
     ChargeBee.update_connect_timeout_secs(connect_timeout)

def update_read_timeout_secs(read_timeout):
     ChargeBee.update_read_timeout_secs(read_timeout)