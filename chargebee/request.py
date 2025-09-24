import json
import urllib

from chargebee import compat, environment, util, http_request
from chargebee.responses import Response


def lowercase_keys(data):
    if isinstance(data, dict):
        return {
            (k if k.startswith("cf_") else k.lower()): lowercase_keys(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [lowercase_keys(item) for item in data]
    else:
        return data


def send_list_request(
    method,
    url,
    env: environment.Environment = None,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
    options=None,
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
        options,
    )


def send(
    method,
    url,
    env: environment.Environment,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
    options=None,
):
    params = lowercase_keys(params)

    if params is None:
        params = {}

    ser_params = (
        params if isJsonRequest else util.serialize(params, None, None, jsonKeys)
    )

    request_args = {
        "method": method,
        "url": url,
        "env": env,
        "params": ser_params,
        "headers": headers,
        "subDomain": subDomain,
        "isJsonRequest": isJsonRequest,
        "options": options,
        "use_async_client": env.use_async_client,
    }

    if env.use_async_client:

        async def async_request():
            response, response_headers, http_code = await http_request.request(
                **request_args
            )
            return Response(
                response_type, response, response_headers, http_code
            ).parse()

        return async_request()
    else:
        response, response_headers, http_code = http_request.request(**request_args)
        return Response(response_type, response, response_headers, http_code).parse()


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
