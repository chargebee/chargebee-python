import json

from chargebee import util, http_request_async, request


async def send_list_request_async(
    method,
    url,
    env=None,
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
    return await send_async(
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


async def send_async(
    method,
    url,
    env,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
    options=None,
):
    params = request.lowercase_keys(params)

    if params is None:
        params = {}

    ser_params = (
        json.dumps(params)
        if isJsonRequest
        else util.serialize(params, None, None, jsonKeys)
    )

    response, response_headers, http_code = await http_request_async.request_async(
        method, url, env, ser_params, headers, subDomain, isJsonRequest, options
    )

    from chargebee.responses import Response

    if "list" in response:
        return Response(
            response_type, response, response_headers, http_code
        ).parse_list_response()
    return Response(
        response_type, response, response_headers, http_code
    ).parse_response()


# Reuse uri_path from request module
uri_path = request.uri_path