from chargebee import util, http
from chargebee.main import ChargeBee
from chargebee.compat import json


def send(method, url, params=None):
    if params is None:
        params = {}

    env = params.pop('env', ChargeBee.default_env)

    ser_params = util.serialize(params)

    response = json.loads(http.request(method, url, env, ser_params))

    from chargebee.result import Result
    from chargebee.list_result import ListResult

    if 'list' in response:
        return ListResult(response['list'])

    return Result(response)

