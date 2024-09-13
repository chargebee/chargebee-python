import urllib
from chargebee import util, http_request
from chargebee.main import ChargeBee
from chargebee import compat
import json


def lowercase_keys(data):
    if isinstance(data, dict):
        return {k.lower(): lowercase_keys(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [lowercase_keys(item) for item in data]
    else:
        return data


def send_list_request(
    method, url, params=None, env=None, headers=None, response_type=None
):
    serialized = {}

    if params is None:
        params = {}

    for k, v in list(params.items()):
        if isinstance(v, list):
            v = json.dumps(v)
        serialized.update({k: v})
    return send(method, url, serialized, env, headers, response_type)


def send(method, url, params=None, env=None, headers=None, response_type=None):
    params = lowercase_keys(params)

    if params is None:
        params = {}

    env = env or ChargeBee.default_env

    ser_params = util.serialize(params)

    response, response_headers = http_request.request(
        method, url, env, ser_params, headers
    )

    from chargebee.responses import Response

    if "list" in response:
        return Response(response_type, response, response_headers).parse_list_response()
    return Response(response_type, response, response_headers).parse_response()


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
