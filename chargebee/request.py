import json

from chargebee import util, http
from chargebee.main import ChargeBee
from chargebee.result import Result
from chargebee.list_result import ListResult


def send(method, url, params=None, env=None):
    env = env or ChargeBee.default_env

    if params is None:
        params = {}

    ser_params = util.serialize(params)

    response = json.loads(http.request(method, url, env, ser_params).read())

    if 'list' in response:
        return ListResult(response['list'])

    return Result(response)
