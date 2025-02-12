import json
import urllib

from chargebee import compat
from chargebee import util, http_request


def lowercase_keys(data):
    if isinstance(data, dict):
        return {k.lower(): lowercase_keys(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [lowercase_keys(item) for item in data]
    else:
        return data


def send_list_request(
    method,
    url,
    env=None,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
):
    serialized = {}

    if params is None:
        params = {}

    for k, v in list(params.items()):
        if isinstance(v, list):
            v = json.dumps(v)
        serialized.update({k: v})
    return send(
        method,
        url,
        env,
        serialized,
        headers,
        response_type,
        subDomain,
        isJsonRequest,
        jsonKeys,
    )


def send(
    method,
    url,
    env,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
):
    params = lowercase_keys(params)

    if params is None:
        params = {}

    ser_params = (
        json.dumps(params)
        if isJsonRequest
        else util.serialize(params, None, None, jsonKeys)
    )

    response, response_headers, http_code = http_request.request(
        method, url, env, ser_params, headers, subDomain, isJsonRequest
    )

    from chargebee.responses import Response

    if "list" in response:
        return Response(
            response_type, response, response_headers, http_code
        ).parse_list_response()
    return Response(
        response_type, response, response_headers, http_code
    ).parse_response()


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
