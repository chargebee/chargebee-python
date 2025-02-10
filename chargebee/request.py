import urllib
from chargebee import util, http_request
from chargebee.main import ChargeBee
from chargebee import compat
import json


def send_list_request(method, url, params=None, env=None, headers=None, subDomain=None, isJsonRequest=None, json_keys=None):
    serialized = {}

    if params is None:
        params = {}

    for k, v in list(params.items()):
        if isinstance(v, list):
            v = json.dumps(v)
        serialized.update({k: v})
    return send(method, url, serialized, env, headers, subDomain, isJsonRequest=None, json_keys=None)


def send(method, url, params=None, env=None, headers=None, subDomain=None, isJsonRequest=None, json_keys=None):
    if params is None:
        params = {}

    env = env or ChargeBee.default_env

    ser_params = json.dumps(params) if isJsonRequest else util.serialize(params,None, None, json_keys)

    response, response_headers, http_status_code = http_request.request(method, url, env, ser_params, headers, subDomain, isJsonRequest)

    from chargebee.result import Result
    from chargebee.list_result import ListResult
    if 'list' in response:
        return ListResult(response['list'], response.get('next_offset', None), response_headers, http_status_code)
    return Result(response, response_headers, http_status_code)


def uri_path(*paths):
    url = ""
    for path in paths:
        if path is None or len(str(path).strip()) < 1:
            raise Exception("Id is None or empty")
        if compat.py_major_v >= 3:
            url = url + "/" + urllib.parse.quote(str(path).strip())
        else:
            url = url + "/" + urllib.quote(str(util.get_val(path)))
    return url
