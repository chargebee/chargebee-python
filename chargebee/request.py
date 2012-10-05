#from chargebee import

from chargebee import util, rest


def send(method, url, params=None, env=None):
    #env = env or ChargeBee.default_env

    if params is None:
        params = {}

    ser_params = util.serialize(params)

    response = rest.request(method, url, env, ser_params)